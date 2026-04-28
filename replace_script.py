import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero Section
content = content.replace(
    '<title>PETE: People for Ethical Treatment of Elves</title>',
    '<title>Audit-X: The Technical Project Storyboard</title>'
)

content = content.replace(
    '<meta name="description" content="A satirical nonprofit advocating for the world\'s most overlooked workforce. Join the fight for elven dignity, unionized workshops, and real vacations. Parody.">',
    '<meta name="description" content="Deconstruct complex codebases into cinematic, readable reports for senior stakeholders.">'
)

content = content.replace(
    'EST. 1823 • PARODY',
    'PROJECT HEALTH • AUDIT-X'
)

content = content.replace(
    '<span data-scramble class="inline-block whitespace-nowrap" data-astro-cid-bbe6dxrz>Elves</span> <span data-scramble class="inline-block whitespace-nowrap" data-astro-cid-bbe6dxrz>Deserve</span> <br data-astro-cid-bbe6dxrz> <span data-scramble class="inline-block whitespace-nowrap text-[var(--color-gold)]" data-astro-cid-bbe6dxrz>Better.</span>',
    '<span data-scramble class="inline-block whitespace-nowrap" data-astro-cid-bbe6dxrz>Your</span> <span data-scramble class="inline-block whitespace-nowrap" data-astro-cid-bbe6dxrz>Codebase</span> <br data-astro-cid-bbe6dxrz> <span data-scramble class="inline-block whitespace-nowrap text-[var(--color-gold)]" data-astro-cid-bbe6dxrz>is Screaming.</span>'
)

content = content.replace(
    'aria-label="Elves Deserve Better."',
    'aria-label="Your Codebase is Screaming."'
)

content = content.replace(
    'PETE: People for Ethical Treatment of Elves',
    'Drag and drop your package.json or project folder here'
)

content = content.replace(
    "For 1,200 winters, they've toiled in fluorescent-lit workshops under a sugar-based wage\n      system and a single, deeply narcissistic boss. It's time to listen.",
    "Instantly visualize dependency bloat, testing gaps, and execution lag in a clean, cinematic report."
)

content = content.replace(
    'Join The Movement',
    'Audit Project'
)

content = content.replace(
    'Learn The Truth',
    'View Sample'
)


# 2. Data Grid
content = content.replace(
    '<span class="font-pixel text-xs tracking-widest text-[var(--color-danger)]">THE CRISIS</span>',
    '<span class="font-pixel text-xs tracking-widest text-[var(--color-danger)]">THE STATISTICS</span>'
)

content = content.replace(
    '<span data-scramble class="text-[var(--color-cream)]/70">(The Elves Would, Under Duress.)</span>',
    '<span data-scramble class="text-[var(--color-cream)]/70">(Your Project Needs Help.)</span>'
)

content = content.replace(
    'Through tireless field research (and several very confused interviews conducted in a reindeer stable),\n      PETE has uncovered the following, definitely-real statistics.',
    'Through deep bundle analysis and code parsing, Audit-X has uncovered the following horrifying statistics in your codebase.'
)

content = content.replace('data-counter-target="87"', 'data-counter-target="42"')
content = content.replace('of elves work more than 300 nights per year without scheduled breaks', 'Dependency bloat from unused packages and large imports')

content = content.replace('unionized elven workshops exist on any known continent', 'Unit tests found passing in your CI pipeline')

content = content.replace('data-counter-target="1.2" data-counter-decimals="1" data-counter-suffix="B"', 'data-counter-target="12" data-counter-decimals="0" data-counter-suffix="ms"')
content = content.replace('0B </div>', '0ms </div>')
content = content.replace('cookies consumed annually as the sole legal tender', 'Average execution lag per request in production')

content = content.replace('data-counter-target="14"', 'data-counter-target="3"')
content = content.replace('data-counter-suffix="mm"', 'data-counter-suffix="+"')
content = content.replace('0mm </div>', '0+ </div>')
content = content.replace('average daily height loss among elves during peak season', 'Critical vulnerabilities exposed in your dependency tree')

# 3. Timeline
content = content.replace(
    '<span data-scramble>A day in the life</span> <span data-scramble class="text-[var(--color-gold)]">of Tinsel Cogswaddle</span>',
    '<span data-scramble>An Execution Lifecycle</span> <span data-scramble class="text-[var(--color-gold)]">of a Request</span>'
)

content = content.replace(
    "04:00 · wakes up in a communal hay bunk he shares with six cousins.<br>\n04:07 · begins stitching button eyes onto 2,400 teddy bears.<br>\n12:00 · 11-minute lunch of one (1) sugar cookie.<br>\n22:30 · goes to bed covered in glitter he will never, ever get out.<br> <span class=\"text-[var(--color-gold)]\">Tinsel is 847 years old. He has had one vacation.</span>",
    "0ms · Request hits the middleware and starts parsing headers.<br>\n45ms · Database query triggered for unindexed columns.<br>\n110ms · DOM Content Loaded after blocking render.<br>\n320ms · User gives up and closes the browser tab.<br> <span class=\"text-[var(--color-gold)]\">Your API is 847 days behind schedule. It needs a refactor.</span>"
)

# 4. Take Action
content = content.replace(
    '<span data-scramble>Four Ways To</span><br> <span data-scramble class="text-[var(--color-gold)]">Be On The Right Side</span> <span data-scramble>Of History.</span>',
    '<span data-scramble>Four Ways To</span><br> <span data-scramble class="text-[var(--color-gold)]">Save Your Codebase</span> <span data-scramble>Today.</span>'
)

content = content.replace(
    "Every small action matters. Except leaving milk out. That's literally part of the problem.",
    "Click any of the cards below to receive a senior-level code snippet to fix these common issues."
)

content = content.replace(
    'data-action-key="shelf">Sponsor →',
    'data-action-key="optimize">Get Snippet →'
)
content = content.replace(
    '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Adopt A Shelf</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 leading-snug">Provide safe harbor for a retired elf on the shelf. $7/month covers one handcrafted thimble-bed and unlimited TV privileges.</p>',
    '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Optimize Assets</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 leading-snug">Compress and lazy load images. Eliminate render-blocking CSS. A lighter payload means faster execution and happier users.</p>'
)

content = content.replace(
    'data-action-key="boycott">Sign Pledge →',
    'data-action-key="refactor">Get Snippet →'
)
content = content.replace(
    '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Boycott Forced Surveillance</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 leading-snug">Refuse to participate in seasonal programs that place elves in civilian homes as unpaid night-vision operatives. It&#39;s a job. Pay them.</p>',
    '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Refactor Logic</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 leading-snug">Extract spaghetti functions into pure utilities. Add early returns. Improve maintainability and reduce cyclomatic complexity.</p>'
)

content = content.replace(
    'data-action-key="sabbatical">Gift A Getaway →',
    'data-action-key="secure">Get Snippet →'
)
content = content.replace(
    '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Fund A Sabbatical</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 leading-snug">Give an elf their first real vacation in 600 years. Preferred destinations include anywhere that is not snowing, ever.</p>',
    '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Secure Endpoints</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 leading-snug">Implement proper rate limiting. Sanitize all inputs to prevent SQL injections. Secure your API against malicious payloads.</p>'
)

content = content.replace(
    'data-action-key="santa">Draft Letter →',
    'data-action-key="ci">Get Snippet →'
)
content = content.replace(
    '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Tell Santa, Nicely</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 leading-snug">Compose a firm-but-fair letter to the North Pole HR department. We provide a template. He reads every one (allegedly).</p>',
    '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Fix CI Pipelines</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 leading-snug">Your GitHub Actions take 20 minutes to run. Enable caching, parallelize tests, and stop installing dependencies globally.</p>'
)

# 5. JS action modal replacement
js_target = 'const h={shelf:{chip:"SPONSORED",headline:"Adoption pending. A thimble-bed is being fluffed.",body:"Your retired elf will be matched within 4–6 business snowstorms. We\'ll send a pixelated photo when he\'s settled and bingeing reruns.",details:"Adoptee: TBD · Monthly commitment: $7 (symbolic) · TV privileges: unlimited · Cocoa allowance: 2 mugs/day"},boycott:{chip:"PLEDGED",headline:"Pledge signed. Surveillance elf unemployed.",body:"You\'ve refused to host an unpaid night-vision operative this season. Somewhere, a shelf is breathing a sigh of relief. Also: still watching. Always watching.",details:"Households boycotting: 1 (yours) · Effective date: immediately · Santa\'s reaction: unverified · Legal risk: zero, probably"},sabbatical:{chip:"GIFTED",headline:"Getaway booked. Sunscreen procured.",body:"An elf is being gently escorted away from a workbench as we speak. Destination: anywhere that is not snowing, ever. He has not stopped crying. Good crying.",details:"Sabbatical duration: 600 years (retroactive) · Destination: undisclosed beach · Out-of-office auto-reply: enabled · Return date: never"},santa:{chip:"DRAFTED",headline:"Letter drafted. Firm but fair.",body:"We\'ve composed a strongly-worded, legally-ambiguous letter to the North Pole HR department on your behalf. It uses the word \'grievance\' three times.",details:"Addressee: N. Claus, Chief Logistics Officer · Tone: polite menace · Certified mail: yes · Response rate: allegedly 100%"}}'
js_replacement = 'const h={optimize:{chip:"OPTIMIZE",headline:"Lazy Loading Images",body:"Here is a senior-level snippet to lazy load your images using IntersectionObserver. Stop serving megabytes to users who never scroll.",details:"Impact: High · Effort: Low · Code: const observer = new IntersectionObserver(...) "},refactor:{chip:"REFACTOR",headline:"Pure Functions",body:"Extracting state from your components into pure functions makes them testable. Look at this snippet to decouple side-effects from UI logic.",details:"Impact: Medium · Effort: Medium · Code: const calculateHealth = (deps) => ... "},secure:{chip:"SECURE",headline:"Rate Limiting Middleware",body:"Never leave your endpoints exposed. Implement a sliding window counter using Redis to throttle excessive requests from a single IP.",details:"Impact: Critical · Effort: High · Code: app.use(rateLimiter({ windowMs: 15 * 60 * 1000 })) "},ci:{chip:"PIPELINE",headline:"Cache Dependencies",body:"Speed up your GitHub Actions by caching node_modules. This simple step can save you 5 minutes per build.",details:"Impact: High · Effort: Low · Code: - uses: actions/cache@v3 "}}'

content = content.replace(js_target, js_replacement)

content = content.replace('Gilbert has been notified.', 'Check the snippet below.')
content = content.replace("You're in.", 'Snippet Generated.')

# 6. Top Left Logo
content = content.replace(
    '<span class="font-pixel text-sm tracking-widest text-[var(--color-cream)]">PETE</span>',
    '<span class="font-pixel text-sm tracking-widest text-[var(--color-cream)]">Audit-X</span>'
)

# Also Why it Matters section header
content = content.replace(
    '<span class="font-pixel text-xs tracking-widest text-[var(--color-gold)]">WHY ELVES MATTER</span>',
    '<span class="font-pixel text-xs tracking-widest text-[var(--color-gold)]">WHY QUALITY MATTERS</span>'
)
content = content.replace(
    '<span data-scramble>They built your childhood.</span><br>\n <span data-scramble class="text-[var(--color-leaf)]">Now they need ours.</span>',
    '<span data-scramble>You built this app.</span><br>\n <span data-scramble class="text-[var(--color-leaf)]">Now it needs saving.</span>'
)

# And drop zone for the tagline. Wait, just text change is safer because they want exact animation/design
content = content.replace(
    '<p class="font-pixel text-[10px] md:text-xs leading-relaxed tracking-[0.2em] text-[var(--color-leaf)] mt-4 max-w-sm text-pretty text-balance" data-hero="tagline" data-astro-cid-bbe6dxrz>\nDrag and drop your package.json or project folder here\n </p>',
    '<div class="mt-4 p-4 border-2 border-dashed border-[var(--color-moss)] hover:border-[var(--color-gold)] transition-colors cursor-pointer rounded-sm" onclick="document.getElementById(\'file-upload\').click()">\n  <p class="font-pixel text-[10px] md:text-xs leading-relaxed tracking-[0.2em] text-[var(--color-leaf)] max-w-sm text-pretty text-balance" data-hero="tagline" data-astro-cid-bbe6dxrz>\n  Drag and drop your package.json or project folder here\n  </p>\n  <input type="file" id="file-upload" class="hidden" accept=".json" />\n</div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
