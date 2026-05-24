import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

copilot_html = '''
<!-- Copilot UI -->
<div id="copilot-container" class="fixed bottom-6 right-6 z-[100] flex flex-col items-end pointer-events-none">
  <!-- Chat Window -->
  <div id="copilot-window" class="hidden pointer-events-auto mb-4 w-80 md:w-96 max-h-[500px] bg-[rgba(11,21,16,0.95)] backdrop-blur-md border-4 border-[var(--color-moss)] flex flex-col shadow-2xl transition-all duration-300 transform translate-y-4 opacity-0">
    <!-- Header -->
    <div class="bg-[var(--color-moss)] p-3 border-b-4 border-[var(--color-moss)] flex justify-between items-center">
      <span class="font-pixel text-xs text-[var(--color-cream)]">Audit-X Copilot</span>
      <button id="copilot-close" class="text-[var(--color-cream)] hover:text-[var(--color-gold)] font-pixel text-xs">X</button>
    </div>
    <!-- Messages -->
    <div id="copilot-messages" class="flex-1 p-4 overflow-y-auto flex flex-col gap-3 font-retro text-sm text-[var(--color-cream)] max-h-80 scrollbar-thin scrollbar-thumb-[var(--color-moss)]">
      <div class="bg-[var(--color-moss)]/50 p-2 border-l-2 border-[var(--color-gold)] self-start max-w-[85%] text-balance">
        Hey bro, I'm the Audit-X Copilot. Drop a package.json or ask me how to use this site.
      </div>
    </div>
    <!-- Input -->
    <div class="p-3 border-t-4 border-[var(--color-moss)] flex gap-2">
      <input type="text" id="copilot-input" class="flex-1 bg-transparent border-2 border-[var(--color-moss)] text-[var(--color-cream)] font-retro text-sm p-2 focus:outline-none focus:border-[var(--color-gold)]" placeholder="Ask about Audit-X...">
      <button id="copilot-send" class="pixel-btn !py-2 !px-3 text-[10px] whitespace-nowrap">SEND</button>
    </div>
  </div>

  <!-- Toggle Button -->
  <button id="copilot-toggle" class="pointer-events-auto pixel-btn flex items-center justify-center shadow-lg" aria-label="Open Copilot">
    <span class="font-pixel text-xs">🤖 Copilot</span>
  </button>
</div>

<script type="module">
  const toggleBtn = document.getElementById('copilot-toggle');
  const closeBtn = document.getElementById('copilot-close');
  const chatWindow = document.getElementById('copilot-window');
  const messagesContainer = document.getElementById('copilot-messages');
  const inputField = document.getElementById('copilot-input');
  const sendBtn = document.getElementById('copilot-send');
  
  const apiKey = import.meta.env.VITE_GROQ_API_KEY;

  let chatHistory = [];
  const systemInstruction = {
    parts: [{ text: "You are the Audit-X Copilot. Audit-X is a codebase analyzer storyboard built by Sunil Yogi (ui/ux designer and developer). Users can drag and drop a package.json file to get a health score, dependency bloat stats, and mock execution lag. They can also click 'Take Action' buttons to get refactoring snippets via mock audit receipts. Answer questions concisely (2-3 sentences), matching the retro 8-bit developer vibe of the site. Be helpful and sarcastic about bad code." }]
  };

  function toggleChat() {
    const isHidden = chatWindow.classList.contains('hidden');
    if (isHidden) {
      chatWindow.classList.remove('hidden');
      setTimeout(() => {
        chatWindow.classList.remove('translate-y-4', 'opacity-0');
      }, 10);
    } else {
      chatWindow.classList.add('translate-y-4', 'opacity-0');
      setTimeout(() => {
        chatWindow.classList.add('hidden');
      }, 300);
    }
  }

  toggleBtn.addEventListener('click', toggleChat);
  closeBtn.addEventListener('click', toggleChat);

  function appendMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `p-2 max-w-[85%] text-balance font-retro text-sm ${sender === 'user' ? 'bg-[var(--color-gold)]/20 border-r-2 border-[var(--color-gold)] self-end text-right' : 'bg-[var(--color-moss)]/50 border-l-2 border-[var(--color-gold)] self-start text-left'}`;
    msgDiv.innerHTML = text.replace(/\\n/g, '<br>').replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>');
    messagesContainer.appendChild(msgDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  }

  async function sendMessage() {
    const text = inputField.value.trim();
    if (!text) return;
    
    inputField.value = '';
    appendMessage(text, 'user');
    
    const loadingId = 'loading-' + Date.now();
    const loadingDiv = document.createElement('div');
    loadingDiv.id = loadingId;
    loadingDiv.className = 'p-2 max-w-[85%] text-balance font-retro text-sm bg-[var(--color-moss)]/50 border-l-2 border-[var(--color-gold)] self-start text-left animate-pulse';
    loadingDiv.textContent = 'Thinking...';
    messagesContainer.appendChild(loadingDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    chatHistory.push({ role: "user", parts: [{ text }] });

    try {
      const groqMessages = [
        { role: 'system', content: systemInstruction.parts[0].text },
        ...chatHistory.map(msg => ({ role: msg.role === 'model' ? 'assistant' : 'user', content: msg.parts[0].text }))
      ];

      const res = await fetch(`https://api.groq.com/openai/v1/chat/completions`, {
        method: 'POST',
        headers: { 
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({ 
          model: 'llama3-8b-8192',
          messages: groqMessages
        })
      });
      const data = await res.json();
      
      const loadEl = document.getElementById(loadingId);
      if(loadEl) loadEl.remove();

      if (data.choices && data.choices[0].message) {
        const reply = data.choices[0].message.content;
        chatHistory.push({ role: "model", parts: [{ text: reply }] });
        appendMessage(reply, 'model');
      } else {
        appendMessage('Error: No response from Groq.', 'model');
      }
    } catch (err) {
      const loadEl = document.getElementById(loadingId);
      if(loadEl) loadEl.remove();
      appendMessage('Connection error. Check your API key or network.', 'model');
    }
  }

  sendBtn.addEventListener('click', sendMessage);
  inputField.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendMessage();
  });
</script>
</body>'''

content = content.replace('</body>', copilot_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Copilot injected successfully.')
