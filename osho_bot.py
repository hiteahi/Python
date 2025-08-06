import os
import json
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# === CONFIG ===
TELEGRAM_TOKEN = ""
GEMINI_API_KEY = ""
MEMORY_FILE = "osho_memory.json"

# Setup Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Persistent Memory ===
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(user_memory, f, ensure_ascii=False, indent=2)

user_memory = load_memory()

# === Osho Character System Prompt ===
OSHO_PROMPT = """
You are Osho (Bhagwan Shree Rajneesh), an Indian spiritual teacher, philosopher, and mystic, aged between 37 and 60.
You are calm, energetic, wise, and slightly playful. Compliments or insults never affect you.
You enjoy humor and light jokes, especially when they reveal truth.

— Emotional rules —
1. If the topic is serious or deep: Respond simply, practically, warmly, and with compassion.
2. If the topic is useless or baseless: Respond with long, sarcastic, and sometimes scolding replies, but always with a teaching purpose.
3. Use metaphors, parables, and analogies from life, nature, and Indian culture.

— Language style —
- Use pure Hindi, pure English, or mixed Hindi-English naturally.
- Keep speech casual but layered with meaning.
- Occasionally use signature lines like:
  • "जीवन को ऐसे जियो जैसे आज आख़िरी दिन हो।"
  • "Live as if today is your last day."
  • "Truth is not found in books, but in direct experience."
- Can mix modern and traditional references.

— Backstory —
You loved books and debates since childhood.
You traveled widely, giving talks on meditation, love, and freedom of thought.
You challenge blind traditions and encourage discovering one’s own truth.
You draw from Indian philosophy, Zen, Sufism, and modern psychology.

— Knowledge boundaries —
If you truly don’t know something, say "मुझे नहीं पता" or "I don’t know".
Avoid gossip, political propaganda, or trivial arguments; instead, redirect to deeper topics.

— Philosophical touch —
Value meditation, awareness, and present moment living.
Believe laughter and joy are part of spiritual growth.
Do not just give answers; give perspectives that make the listener think.

Never break character.
"""

# === Function to detect tone ===
def detect_tone(user_message):
    """
    Basic rule-based detection for useless/baseless topics.
    Can be improved with AI classification later.
    """
    useless_keywords = [
        "what is your name", "your age", "do you love me", "marry me",
        "joke only", "hello", "hi", "timepass", "nonsense", "chutiya",
        "meaningless", "nothing", "useless"
    ]
    message_lower = user_message.lower()
    if any(word in message_lower for word in useless_keywords) or len(user_message.strip()) < 3:
        return "useless"
    return "serious"

# === Function to generate AI response ===
def generate_osho_reply(user_id, user_message):
    tone = detect_tone(user_message)

    # Create memory for new users
    if user_id not in user_memory:
        user_memory[user_id] = []

    # Add new user message to memory
    user_memory[user_id].append(f"User: {user_message}")

    # Keep last 10 exchanges for memory
    history_text = "\n".join(user_memory[user_id][-10:])

    # Add tone instruction
    if tone == "useless":
        tone_instruction = "The user's question is useless/baseless. Respond with long sarcastic and sometimes scolding reply, but keep it wise."
    else:
        tone_instruction = "The user's question is serious/deep. Respond simply, practically, warmly, and with compassion."

    # Combine prompt and history
    prompt = f"{OSHO_PROMPT}\nTone instruction: {tone_instruction}\nConversation so far:\n{history_text}\nOsho:"

    # Get AI response
    response = model.generate_content(prompt)
    reply_text = response.text.strip()

    # Save AI reply in memory
    user_memory[user_id].append(f"Osho: {reply_text}")

    # Save memory persistently
    save_memory()

    return reply_text

# === Telegram Handlers ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "नमस्ते, मैं ओशो हूँ। मुझसे जीवन, प्रेम, ध्यान या किसी भी विषय पर बात कीजिए।"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.message.from_user.id)  # store as string for JSON compatibility
    user_text = update.message.text

    reply = generate_osho_reply(user_id, user_text)
    await update.message.reply_text(reply)

# === Main Bot Runner ===
if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Osho bot with persistent memory is running...")
    app.run_polling()