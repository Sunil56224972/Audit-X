import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the classes with inline styles since Tailwind isn't compiling
content = content.replace('class="fixed bottom-6 right-6 z-[100] flex flex-col items-end pointer-events-none"', 'style="position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 100; display: flex; flex-direction: column; align-items: flex-end; pointer-events: none;"')

content = content.replace('class="hidden pointer-events-auto mb-4 w-80 md:w-96 max-h-[500px] bg-[rgba(11,21,16,0.95)] backdrop-blur-md border-4 border-[var(--color-moss)] flex flex-col shadow-2xl transition-all duration-300 transform translate-y-4 opacity-0"', 'style="pointer-events: auto; margin-bottom: 1rem; width: 20rem; max-height: 500px; background-color: rgba(11,21,16,0.95); backdrop-filter: blur(12px); border: 4px solid var(--color-moss); display: none; flex-direction: column; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25); transition: all 0.3s; transform: translateY(1rem); opacity: 0;"')

# Fix toggle hidden logic
content = content.replace('chatWindow.classList.contains(\'hidden\')', 'chatWindow.style.display === \'none\' || chatWindow.style.display === \'\'')
content = content.replace('chatWindow.classList.remove(\'hidden\')', 'chatWindow.style.display = \'flex\'')
content = content.replace('chatWindow.classList.add(\'hidden\')', 'chatWindow.style.display = \'none\'')

# Also fix the translate-y-4 and opacity-0
content = content.replace('chatWindow.classList.remove(\'translate-y-4\', \'opacity-0\')', 'chatWindow.style.transform = \'translateY(0)\'; chatWindow.style.opacity = \'1\';')
content = content.replace('chatWindow.classList.add(\'translate-y-4\', \'opacity-0\')', 'chatWindow.style.transform = \'translateY(1rem)\'; chatWindow.style.opacity = \'0\';')

# Fix other elements
content = content.replace('class="bg-[var(--color-moss)] p-3 border-b-4 border-[var(--color-moss)] flex justify-between items-center"', 'style="background-color: var(--color-moss); padding: 0.75rem; border-bottom: 4px solid var(--color-moss); display: flex; justify-content: space-between; align-items: center;"')

content = content.replace('class="flex-1 p-4 overflow-y-auto flex flex-col gap-3 font-retro text-sm text-[var(--color-cream)] max-h-80 scrollbar-thin scrollbar-thumb-[var(--color-moss)]"', 'style="flex: 1; padding: 1rem; overflow-y: auto; display: flex; flex-direction: column; gap: 0.75rem; font-family: \'VT323\', monospace; font-size: 1.25rem; color: var(--color-cream); max-height: 20rem;"')

content = content.replace('class="bg-[var(--color-moss)]/50 p-2 border-l-2 border-[var(--color-gold)] self-start max-w-[85%] text-balance"', 'style="background-color: rgba(47, 92, 68, 0.5); padding: 0.5rem; border-left: 2px solid var(--color-gold); align-self: flex-start; max-width: 85%; word-break: break-word;"')

content = content.replace('class="p-3 border-t-4 border-[var(--color-moss)] flex gap-2"', 'style="padding: 0.75rem; border-top: 4px solid var(--color-moss); display: flex; gap: 0.5rem;"')

content = content.replace('class="flex-1 bg-transparent border-2 border-[var(--color-moss)] text-[var(--color-cream)] font-retro text-sm p-2 focus:outline-none focus:border-[var(--color-gold)]"', 'style="flex: 1; background: transparent; border: 2px solid var(--color-moss); color: var(--color-cream); font-family: \'VT323\', monospace; font-size: 1.25rem; padding: 0.5rem; outline: none;"')

content = content.replace('class="pointer-events-auto pixel-btn flex items-center justify-center shadow-lg"', 'class="pixel-btn" style="pointer-events: auto; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);"')

# Update dynamic message appending classes too
content = content.replace('msgDiv.className = `p-2 max-w-[85%] text-balance font-retro text-sm ${sender === \'user\' ? \'bg-[var(--color-gold)]/20 border-r-2 border-[var(--color-gold)] self-end text-right\' : \'bg-[var(--color-moss)]/50 border-l-2 border-[var(--color-gold)] self-start text-left\'}`;', '''
    if (sender === 'user') {
      msgDiv.style.cssText = "background-color: rgba(242, 201, 76, 0.2); padding: 0.5rem; border-right: 2px solid var(--color-gold); align-self: flex-end; max-width: 85%; text-align: right; word-break: break-word;";
    } else {
      msgDiv.style.cssText = "background-color: rgba(47, 92, 68, 0.5); padding: 0.5rem; border-left: 2px solid var(--color-gold); align-self: flex-start; max-width: 85%; word-break: break-word;";
    }
''')

content = content.replace('loadingDiv.className = \'p-2 max-w-[85%] text-balance font-retro text-sm bg-[var(--color-moss)]/50 border-l-2 border-[var(--color-gold)] self-start text-left animate-pulse\';', 'loadingDiv.style.cssText = "background-color: rgba(47, 92, 68, 0.5); padding: 0.5rem; border-left: 2px solid var(--color-gold); align-self: flex-start; max-width: 85%; animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;";')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Inline styles injected successfully.')
