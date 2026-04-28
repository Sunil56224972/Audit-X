import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'<h3 class="font-pixel text-sm leading-snug text-\[var\(--color-cream\)\]">Cultural Heritage</h3>\s*<p class="font-retro text-xl text-\[var\(--color-cream\)\]/80 mt-4 leading-snug">Elves have been quietly sustaining seasonal joy since long before recorded history\. Their oral tradition is preserved entirely in limericks\. Lose the elf, lose the limerick\.</p>',
     '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Technical Debt</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 mt-4 leading-snug">Your codebase has been quietly accumulating workarounds and hacks since its inception. Institutional knowledge is preserved entirely in Slack messages. Lose the senior dev, lose the architecture.</p>'),
     
    (r'<h3 class="font-pixel text-sm leading-snug text-\[var\(--color-cream\)\]">Ecological Stewards</h3>\s*<p class="font-retro text-xl text-\[var\(--color-cream\)\]/80 mt-4 leading-snug">Elves maintain 83% of the world&#39;s remaining mushroom circles\. Without their gentle foraging cycle, the entire fairy-industrial complex collapses within two fiscal quarters\.</p>',
     '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">Dependency Stewards</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 mt-4 leading-snug">NPM packages maintain 83% of your application&#39;s remaining core functionality. Without their gentle update cycle, your entire deployment pipeline collapses within two minor version bumps.</p>'),
     
    (r'<h3 class="font-pixel text-sm leading-snug text-\[var\(--color-cream\)\]">The Cookie Economy</h3>\s*<p class="font-retro text-xl text-\[var\(--color-cream\)\]/80 mt-4 leading-snug">An estimated 1\.2 billion cookies circulate through elven supply chains each year\. If elves vanished overnight, your grandmother&#39;s oven would become a speculative asset\.</p>',
     '<h3 class="font-pixel text-sm leading-snug text-[var(--color-cream)]">The Error Economy</h3> <p class="font-retro text-xl text-[var(--color-cream)]/80 mt-4 leading-snug">An estimated 1.2 billion unhandled exceptions circulate through your logging systems each year. If users actually reported them, your Jira backlog would become a speculative asset.</p>'),

    (r'<span data-scramble>They built your childhood\.</span><br>\s*<span data-scramble class="text-\[var\(--color-leaf\)\]">Now they need ours\.</span>',
     '<span data-scramble>They built your prototype.</span><br> <span data-scramble class="text-[var(--color-leaf)]">Now it needs a refactor.</span>'),

    (r'<h3 class="font-pixel text-lg md:text-2xl leading-snug text-\[var\(--color-cream\)\]">\s*<span data-scramble>Donate</span>\s*<span data-scramble class="text-\[var\(--color-gold\)\]">one cookie</span><span data-scramble>\.</span><br>\s*<span data-scramble>Save</span>\s*<span data-scramble class="text-\[var\(--color-leaf\)\]">an entire workshop</span><span data-scramble>\.</span>\s*</h3>',
     '<h3 class="font-pixel text-lg md:text-2xl leading-snug text-[var(--color-cream)]"> <span data-scramble>Refactor</span> <span data-scramble class="text-[var(--color-gold)]">one function</span><span data-scramble>.</span><br> <span data-scramble>Save</span> <span data-scramble class="text-[var(--color-leaf)]">an entire codebase</span><span data-scramble>.</span> </h3>'),

    (r'100% of all donations go directly to elf sabbatical funds, mushroom-circle restoration, and a\s*very comfortable beanbag for the PETE mascot, Gilbert\.',
     '100% of all your effort goes directly to technical debt repayment, continuous integration restoration, and a very comfortable beanbag for the Audit-X mascot, Gilbert.'),

    (r'Donate \$7', 'Refactor UI'),
    (r'Donate \$24', 'Refactor API'),
    (r'Other Amount', 'Full Rewrite'),

    (r'<span class="font-pixel text-xs tracking-widest text-\[var\(--color-leaf\)\]">VOICES OF THE LIBERATED</span>',
     '<span class="font-pixel text-xs tracking-widest text-[var(--color-leaf)]">VOICES OF THE REFACTORED</span>'),

    (r'<span data-scramble>Real elves\.</span><br><span data-scramble class="text-\[var\(--color-gold\)\]">Real\(ish\) stories\.</span>',
     '<span data-scramble>Real devs.</span><br><span data-scramble class="text-[var(--color-gold)]">Real(ish) horror stories.</span>'),

    (r'<blockquote class="font-retro text-xl text-\[var\(--color-cream\)\]/90 leading-snug">I hadn&#39;t slept since 1847\. PETE got me a weighted blanket and a long weekend in Ibiza\. I&#39;m a new elf\.</blockquote>\s*<figcaption class="mt-auto pt-4 border-t-2 border-dashed border-\[var\(--color-moss\)\]">\s*<div class="font-pixel text-\[11px\] text-\[var\(--color-cream\)\]">Twinkle Greenleaf</div>\s*<div class="font-retro text-base text-\[var\(--color-cream\)\]/60 mt-1">Former Sewing Machinist, Workshop 14</div>\s*</figcaption>',
     '<blockquote class="font-retro text-xl text-[var(--color-cream)]/90 leading-snug">I hadn&#39;t seen the sun since 2018. Audit-X found the memory leak and I finally took a weekend off. I&#39;m a new dev.</blockquote> <figcaption class="mt-auto pt-4 border-t-2 border-dashed border-[var(--color-moss)]"> <div class="font-pixel text-[11px] text-[var(--color-cream)]">Travis "Commit" Jenkins</div> <div class="font-retro text-base text-[var(--color-cream)]/60 mt-1">Former 10x Engineer, Startup 14</div> </figcaption>'),

    (r'<blockquote class="font-retro text-xl text-\[var\(--color-cream\)\]/90 leading-snug">For 312 years my only vocabulary was &#39;merry&#39; and &#39;ho&#39;\. Now I have opinions about jazz\. Thank you, PETE\.</blockquote>\s*<figcaption class="mt-auto pt-4 border-t-2 border-dashed border-\[var\(--color-moss\)\]">\s*<div class="font-pixel text-\[11px\] text-\[var\(--color-cream\)\]">Bramble Oakfoot</div>\s*<div class="font-retro text-base text-\[var\(--color-cream\)\]/60 mt-1">Recovering Ornament Stacker</div>\s*</figcaption>',
     '<blockquote class="font-retro text-xl text-[var(--color-cream)]/90 leading-snug">For 3 years my only vocabulary was &#39;npm install&#39; and &#39;sudo&#39;. Now I have opinions about system design. Thank you, Audit-X.</blockquote> <figcaption class="mt-auto pt-4 border-t-2 border-dashed border-[var(--color-moss)]"> <div class="font-pixel text-[11px] text-[var(--color-cream)]">Sarah "Sudo" Bash</div> <div class="font-retro text-base text-[var(--color-cream)]/60 mt-1">Recovering Full-Stack Developer</div> </figcaption>'),

    (r'<blockquote class="font-retro text-xl text-\[var\(--color-cream\)\]/90 leading-snug">They told us the big guy was &#39;family&#39;\. Turns out &#39;family&#39; pays in crumbs\. I walked out\. You can too\.</blockquote>\s*<figcaption class="mt-auto pt-4 border-t-2 border-dashed border-\[var\(--color-moss\)\]">\s*<div class="font-pixel text-\[11px\] text-\[var\(--color-cream\)\]">Mistletoe Fizzwick</div>\s*<div class="font-retro text-base text-\[var\(--color-cream\)\]/60 mt-1">PETE Advocacy Lead, Northern Hemisphere</div>\s*</figcaption>',
     '<blockquote class="font-retro text-xl text-[var(--color-cream)]/90 leading-snug">They told us the startup was &#39;family&#39;. Turns out &#39;family&#39; pays in useless equity. I refactored and walked out. You can too.</blockquote> <figcaption class="mt-auto pt-4 border-t-2 border-dashed border-[var(--color-moss)]"> <div class="font-pixel text-[11px] text-[var(--color-cream)]">Marcus "Merge" Conflict</div> <div class="font-retro text-base text-[var(--color-cream)]/60 mt-1">Audit-X Advocate, Silicon Valley</div> </figcaption>'),

    (r'IN PARTNERSHIP WITH\s*</span>\s*<span class="inline-block w-8 h-\[3px\]" style="background: #d9b3d9;"></span>\s*</div>\s*<h3 class="font-pixel text-xl md:text-3xl leading-snug text-\[var\(--color-cream\)\]">\s*<span data-scramble>PETE</span>\s*<span data-scramble style="color: #d9b3d9;">×</span>\s*<span data-scramble style="color: #f2c94c;">PETU</span>\s*</h3>\s*<p class="font-retro text-xl md:text-2xl text-\[var\(--color-cream\)\]/85 mt-3 max-w-xl">\s*We\'ve joined forces with our horned counterparts at\s*<strong style="color: #d9b3d9;">PETU</strong>,\s*the People for Ethical Treatment of Unicorns\. Because elves deserve unions,\s*and unicorns deserve more than glitter-based compensation\.\s*</p>\s*<p class="font-retro text-lg text-\[var\(--color-cream\)\]/70 mt-3 max-w-xl">\s*Stop the rainbow extraction\. End the birthday-party gig economy\. Pay the horn tax\.\s*</p>\s*</div>\s*<div class="flex justify-center md:justify-end">\s*<a href="https://petu\.info" target="_blank" rel="noopener noreferrer" class="pixel-btn" style="background: #d9b3d9; border-color: var\(--color-cream\);">\s*Visit PETU →\s*</a>',
     'IN PARTNERSHIP WITH\n</span> <span class="inline-block w-8 h-[3px]" style="background: #d9b3d9;"></span> </div> <h3 class="font-pixel text-xl md:text-3xl leading-snug text-[var(--color-cream)]"> <span data-scramble>Audit-X</span> <span data-scramble style="color: #d9b3d9;">×</span> <span data-scramble style="color: #f2c94c;">Audit-Y</span> </h3> <p class="font-retro text-xl md:text-2xl text-[var(--color-cream)]/85 mt-3 max-w-xl">\nWe\'ve joined forces with our frontend counterparts at\n<strong style="color: #d9b3d9;">Audit-Y</strong>,\n            the Auditors for React and Next.js. Because backends deserve optimization,\n            and frontends deserve more than CSS-in-JS based bloat.\n</p> <p class="font-retro text-lg text-[var(--color-cream)]/70 mt-3 max-w-xl">\nStop the bundle bloat. End the hydration mismatch economy. Pay the tech debt tax.\n</p> </div> <div class="flex justify-center md:justify-end"> <a href="#" target="_blank" rel="noopener noreferrer" class="pixel-btn" style="background: #d9b3d9; border-color: var(--color-cream);">\nVisit Audit-Y →\n</a>'),

    (r'FOUNDER · PETU', 'FOUNDER · AUDIT-Y'),
    
    (r'Horn-rights advocate\. Former glitter auditor\. Currently unreachable\. On sabbatical with a unicorn\.',
     'Frontend performance advocate. Former div auditor. Currently unreachable. On sabbatical writing raw HTML.'),

    (r'People for Ethical Treatment of Elves\. A satirical nonprofit parody\. No elves \(or humans\) were\s*harmed in the making of this site\.',
     'Audit-X. A technical project storyboard. No servers (or developers) were\n        harmed in the making of this site.'),

    (r'PARODY SITE • NOT AFFILIATED WITH ANY NORTHERN OPERATION',
     'AUDIT-X • NOT AFFILIATED WITH ANY AGILE CONSULTANCY'),

    (r'Thank you for your \(imaginary\) donation!', 'Thank you for your (imaginary) refactor!'),
    (r'100% of your \$0\.00 has been routed to Gilbert, the PETE mascot\. He used it to buy a beanbag\. He\'s very happy\.',
     '100% of your effort has been routed to Gilbert, the Audit-X mascot. He used it to buy more RAM. He\'s very happy.'),
    (r'An elf has been notified of your generosity\.', 'A developer has been notified of your code review.'),
    (r'He is currently weeping softly into a thimble of hot cocoa\. We\'re told these are tears of joy\. We cannot confirm\.',
     'They are currently weeping softly into a mechanical keyboard. We\'re told these are tears of joy. We cannot confirm.'),
    (r'Donation received\. Forwarding to sabbatical fund\.', 'Refactor received. Forwarding to production environment.'),
    (r'Pending approval from the Chief Elf Officer, who is currently on a sabbatical we have not yet funded\. A classic\.',
     'Pending approval from the Chief Technical Officer, who is currently on a sabbatical we have not yet funded. A classic.'),
    (r'We\'ve sent a very strongly-worded thank-you letter to the North Pole HR department on your behalf\. No reply yet\.',
     'We\'ve sent a very strongly-worded PR comment to the infrastructure department on your behalf. No reply yet.'),
    (r'You donated a cookie\. Legally, that\'s enough\.', 'You refactored a function. Legally, that\'s enough.'),
    (r'Please leave it on the monitor\. A PETE field agent will retrieve it at 2:47 AM local time\. Do not watch\.',
     'Please leave it in the main branch. An Audit-X field agent will review it at 2:47 AM local time. Do not watch.'),
    (r'No elves were tipped\.', 'No developers were tipped.'),
    (r'Tipping elves is, counterintuitively, considered extremely rude\. Union rules\. We\'re working on it\.',
     'Tipping developers is, counterintuitively, considered extremely rude. Agile rules. We\'re working on it.'),
    (r'\{"Donate \$7":"\$7\.00","Donate \$24":"\$24\.00","Other Amount":"\$∞",Donate:"\$0\.00","Donate Again":"\$0\.00"\}',
     '{"Refactor UI":"$7.00","Refactor API":"$24.00","Full Rewrite":"$∞","Audit Project":"$0.00","Refactor Again":"$0.00"}'),
    
    (r'Donate Again', 'Refactor Again'),
    
    (r'Why Elves Matter', 'Why Tech Debt Matters')
]

for pattern, repl in replacements:
    content, count = re.subn(pattern, repl, content)
    print(f"Replaced {count} occurrences of pattern: {pattern[:30]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finished!")
