# links

[![Build Status](https://github.com/pawroman/links/workflows/Test/badge.svg)](https://github.com/pawroman/links/actions)
![Python version used for testing](https://img.shields.io/badge/Python-3.9-blue.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Links to programming related resources I found useful or interesting.
A personal "awesome list".

You can find out more about me at: [pawroman.dev](https://pawroman.dev)

All the links are tested after every commit and daily using
[lychee](https://github.com/lycheeverse/lychee)
via [GitHub Actions](https://github.com/pawroman/links/actions),
but if you see anything that's not working, please let me know!

## Table of Contents

- [Prelude](#prelude)
- [Other Lists](#other-lists)
- [Algorithms](#algorithms)
- [Architecture and Programming Patterns](#architecture-and-programming-patterns)
- [Assorted "How Stuff Works"](#assorted-how-stuff-works)
- [Career Development](#career-development)
- [Code Quality and Good Practices](#code-quality-and-good-practices)
- [Command Line Tools](#command-line-tools)
    - [GUI tools](#gui-tools)
- [Data](#data)
    - [Databases](#databases)
- [Design and Web](#design-and-web)
- [Distributed Systems and Cloud Computing](#distributed-systems-and-cloud-computing)
- [Docker](#docker)
- [Eye Candy](#eye-candy)
    - [Fonts](#fonts)
    - [Themes](#themes)
- [git](#git)
    - [git help](#git-help)
- [Go](#go)
- [Hardware and CPUs](#hardware-and-cpus)
- [Kubernetes](#kubernetes)
- [Linux](#linux)
- [Management / dealing with people](#management--dealing-with-people)
- [Networking](#networking)
- [Privacy](#privacy)
- [Productivity](#productivity)
- [Programming Languages](#programming-languages)
- [Python](#python)
    - [Python learning](#python-learning)
    - [Python libraries](#python-libraries)
    - [Python news and community](#python-news-and-community)
    - [Python tools](#python-tools)
- [Rust](#rust)
    - [Rust learning](#rust-learning)
    - [Rust libraries](#rust-libraries)
    - [Rust news and community](#rust-news-and-community)
    - [Rust posts and talks](#rust-posts-and-talks)
    - [Rust tools](#rust-tools)
- [Shell](#shell)
- [Testing](#testing)
    - [Static analysis](#static-analysis)
- [Visualization](#visualization)

---

## Prelude

Some of my favourite quotes:

> *"Craftsmanship over Crap"* \
> -- Uncle Bob

> *"… with proper design, the features come cheaply.
> This approach is arduous, but continues to succeed."* \
> -- Dennis Ritchie

> *"Code is a way you treat your coworkers.
> We interact through the things we make."* \
> -- [Michael Feathers](https://vimeo.com/293912618/5ccecc85d4)

> *"Theory is when you know everything but nothing works. \
> Practice is when everything works but no one knows why. \
> In our lab, theory and practice are combined: nothing works and no one knows why."*

---

## Other Lists

- [Awesome Python](https://github.com/vinta/awesome-python)
- [The Book of Secret Knowledge](https://github.com/trimstray/the-book-of-secret-knowledge)

## Algorithms

Articles:

- [Cache replacement policies](https://en.wikipedia.org/wiki/Cache_replacement_policies)
  \- Algorithms that tell you how to evict entries from the cache.
- [Consistent Hashing](https://en.wikipedia.org/wiki/Consistent_hashing)
  - [The Simple Magic of Consistent Hashing](https://www.paperplanes.de/2011/12/9/the-magic-of-consistent-hashing.html)
  - [The Ultimate Guide to Consistent Hashing](https://www.toptal.com/big-data/consistent-hashing)
- [Dijkstra's in Disguise](https://blog.evjang.com/2018/08/dijkstras.html)
- [In Search of an Understandable Consensus Algorithm](https://raft.github.io/raft.pdf)
  \- (PDF) paper describing the [Raft][raft] consensus algorithm.
- [Introduction to the A* Algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
  \- Explained very clearly, with great interactive examples.
     Also explores BFS and Dijkstra's algorithm.
  - [Implementation of A*](https://www.redblobgames.com/pathfinding/a-star/implementation.html)
    \- A follow up on the article, with implementation tips.
- [Rendezvous hashing](https://en.wikipedia.org/wiki/Rendezvous_hashing)
- [Reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)
  \- Sample items from very large or infinite collections.
- [The Wavefunction Collapse Algorithm explained very clearly](https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/)

Books:

- [Algorithms by Jeff Erickson](http://jeffe.cs.illinois.edu/teaching/algorithms/)
- [The Algorithm Design Manual](https://www.goodreads.com/book/show/10144324-the-algorithm-design-manual)
  \- An excellent resource for all sorts of algorithms, full of references.

Other:

- [Big-O Complexity Cheat Sheet](https://web.archive.org/web/20201202214731/https://www.bigocheatsheet.com/)
- [Raft Consensus Algorithm Visualization](http://thesecretlivesofdata.com/raft/)
  \- [Raft][raft] Visualized in a very easy to follow way.
- [xoshiro / xoroshiro generators and the PRNG shootout](http://xoshiro.di.unimi.it/)
  \- Small and fast Pseudo-Random Number Generators.

[raft]: https://raft.github.io/

## Architecture and Programming Patterns

- [Clean Architecture (book)](https://www.goodreads.com/book/show/18043011-clean-architecture)
- [Design Patterns](https://sourcemaking.com/design_patterns) - Describes the classic OO patterns.
- [Game Programming Patterns](http://gameprogrammingpatterns.com/contents.html)
  \- An excellent book on OO patterns found in games. When performance matters.
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
  \- Concepts behind modern(-ish) large-scale systems, with plenty of references.
- [The Architecture of Open Source Applications](http://www.aosabook.org/en/index.html)
- [The Internals of PostgreSQL](http://www.interdb.jp/pg/)
  \- "for database administrators and system developers".
- [The Twelve-Factor App](https://12factor.net/)
  \- 12 good rules for "service" type software.
- [Vertical Slice Architecture](https://jimmybogard.com/vertical-slice-architecture/)
  \- Argues that architecture should be sliced "vertically" (across business domains)
     rather than "horizontally".
  - [PresentationDomainDataLayering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html)
    \- Similar concept from Martin Fowler.
- [You are not Google](https://blog.bradfieldcs.com/you-are-not-google-84912cf44afb)
  \- Words of caution on architecture and scale.

Anti-patterns:

- [Database-as-IPC](https://en.wikipedia.org/wiki/Database-as-IPC)
- [Global Variables Are Bad](http://wiki.c2.com/?GlobalVariablesAreBad)

Visualizing Architecture:

- [The C4 model for visualizing software architecture](https://c4model.com/)
  \- A promising model for visualizing software.
  - [C4-PlantUML](https://github.com/RicardoNiepel/C4-PlantUML)
    \- A reasonably decent tool, however the diagrams need to contain few elements
       to be readable.
  - [Visualising software architecture with the C4 model (video)](https://www.youtube.com/watch?v=x2-rSnhpw0g)
    \- An introductory talk about this model.

## Assorted "How Stuff Works"

- [How does UTF-8 turn “😂” into “F09F9882”?](https://sethmlarson.dev/blog/utf-8)
  \- A nice walk-through of UTF-8 internals.

## Career Development

- [Apprenticeship Patterns](https://www.oreilly.com/library/view/apprenticeship-patterns/9780596806842/)
  \- Problem-solution book for career planning, in praise of
  [software craftsmanship](https://en.wikipedia.org/wiki/Software_craftsmanship).
  Free to read online.

## Code Quality and Good Practices

The Clean trilogy from Robert C. Martin ("Uncle Bob"):

1. [Clean Code (book)](https://www.goodreads.com/book/show/3735293-clean-code)
2. [The Clean Coder (book)](https://www.goodreads.com/book/show/10284614-the-clean-coder)
3. [Clean Architecture (book)](https://www.goodreads.com/book/show/18043011-clean-architecture)

Programming overall:

- [The Future of Programming (video)](https://www.youtube.com/watch?v=ecIWPzGEbFc)
  \- A talk from Uncle Bob about the past and the future of programming.
     Touches on a plethora of subjects, well worth a watch.
- [The Pragmatic Programmer (book)](https://pragprog.com/titles/tpp20/)
  \- An absolute classic of a book, there's a new 20th Anniversary Edition.
  - [Take-home reference](https://blog.codinghorror.com/a-pragmatic-quick-reference/)
    \- Sums up the book.

Principles:

- [AHA Programming](https://kentcdodds.com/blog/aha-programming)
  \- Avoid Hasty Abstractions.
- [Don't Repeat Yourself](https://en.wikipedia.org/wiki/Don't_repeat_yourself)
  - [DRY (Don't Repeat Yourself) is a Fallacy](https://web.archive.org/web/20190416201841/https://adamcod.es/2017/07/14/dry-is-a-fallacy.html)
    \- Argues that DRY is mostly about **knowledge**, not just code.
- [Make It Work, Make It Right, Make It Fast](http://wiki.c2.com/?MakeItWorkMakeItRightMakeItFast)
- [Principle of least astonishment](https://en.wikipedia.org/wiki/Least_astonishment)
- [Rule of three][rule-of-three]
    \- Rule stating that a generalization should only be attempted on third repetition/duplication.
    - [The Rule of Three](https://andrewbrookins.com/technology/the-rule-of-three/)
      \- Explains the rationale and benefits of this principle.

[rule-of-three]: https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)

Principle aggregates / manifestos:

- [hacker-laws](https://github.com/dwmkerr/hacker-laws)
- [Programming Principles](https://github.com/webpro/programming-principles)
- [Software craftsmanship](https://en.wikipedia.org/wiki/Software_craftsmanship)
    - [Manifesto for Software Craftsmanship](http://manifesto.softwarecraftsmanship.org/)

Code quality measures:

- [Cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)

Legacy / Refactoring / Maintenance:

- [Avoid rewriting a legacy system from scratch, by strangling it](https://understandlegacycode.com/blog/avoid-rewriting-a-legacy-system-from-scratch-by-strangling-it/)
  \- A very reasonable approach to rolling out new systems, without full rewrites.
- [How To Write Unmaintainable Code](https://github.com/Droogans/unmaintainable-code)
  \- Learn what not to do :)
- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
  \- A set of guidelines for maintaining changelogs (aka. change logs) in projects.
     This is a very good practice for versioned software.
- [Preventing the Collapse of Civilization](https://www.youtube.com/watch?v=ZSRHeXYDLko)
  \- A good talk touching on software simplicity and knowledge transfer
     in software development.
- [When costs are nonlinear, keep it small.](https://jessitron.com/2021/01/18/when-costs-are-nonlinear-keep-it-small/)
  \- Talks about the importance of regular maintenance:
   > Do the easy boring job regularly, instead of the hard scary job in a panic.
- [Write code that is easy to delete, not easy to extend.](https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to)
  \- Iterating on code design should be easy.
   > Good code isn't about getting it right the first time.
     Good code is just legacy code that doesn't get in the way.

Other:

- [5 Things I’ve Learned in 20 Years of Programming](https://daedtech.com/5-things-ive-learned-in-20-years-of-programming/)
  \- Some good advice.
- [API Evolution the Right Way](https://emptysqua.re/blog/api-evolution-the-right-way/)
- [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist)
- [ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html)
  \- Advises to document project's architecture in the repo.
- [Do Not Log](https://sobolevn.me/2020/03/do-not-log)
  \- Argues that in certain cases logging should be avoided over more structured
     solutions (monitoring, error tracking).  Recommends Rust patterns in Python :)
- [Empathy is Code Deep](https://vimeo.com/293912618/5ccecc85d4)
  \- A talk on applying empathy and thinking about others in coding.
     Code matters and people do too.
- [Some Useful Probability Facts for Systems Programming](https://theartofmachinery.com/2020/01/27/systems_programming_probability.html)
  \- Probability applies to systems and probabilistic models explain some
     seemingly weird behaviors rather well.
- [Superior Testing: Stop Stopping](https://web.archive.org/web/20190515233744/https://arturdryomov.online/posts/superior-testing-stop-stopping/)
  \- Great post on why testing matters (Archived version).
- [The AI Hierarchy of Needs](https://hackernoon.com/the-ai-hierarchy-of-needs-18f111fcc007)
  \- Looking to do AI? Better sort out the basics and foundations first.
  Contains the "AI pyramid of needs". I would add "Solid engineering" at the
  very bottom of the pyramid though!

## Command Line Tools

- [ArchiveBox](https://github.com/pirate/ArchiveBox)
  \- Your personal (self-hosted) webpage archive.
- [bandwhich](https://github.com/imsnif/bandwhich)
  \- Display current network utilization by process, connection and remote IP/hostname.
- [bat](https://github.com/sharkdp/bat) - Syntax and git-aware `cat` clone, with automated paging.
- [ctop](https://github.com/bcicen/ctop) - `top` for containers.
- [DBCLI](https://www.dbcli.com) - Collection of great CLI database clients,
    e.g. [pgcli](https://www.pgcli.com), [mycli](https://www.mycli.net) etc.
- [dive](https://github.com/wagoodman/dive)
  \- Inspect Docker images, layer by layer.  Useful to search for spurious/unneeded files.
- [dua](https://github.com/Byron/dua-cli)
  \- Aka. `dua-cli`.  A (fast!) disk usage analyzer and cleaner.  Also has a nice interactive mode.
- [exa](https://github.com/ogham/exa) - Better than `ls`.  Also has a `tree`-like switch (`-T`).
- [fd](https://github.com/sharkdp/fd) - Better than `find`.
- [gdb-dashboard](https://github.com/cyrus-and/gdb-dashboard) - Makes GDB so much better.
- [git-quick-stats](https://github.com/arzzen/git-quick-stats)
  \- Get simple statistics for your repo.
- [grex](https://github.com/pemistahl/grex)
  \- Generate regular expressions matching provided inputs.
- [htop](https://github.com/hishamhm/htop) - Excellent process viewer.
- [HTTPie](https://httpie.org/)
  \- cURL for humans. An easy to use CLI HTTP client. Uses Python + requests. Also see `xh`.
- [hyperfine](https://github.com/sharkdp/hyperfine) - CLI benchmarking tool.
- [iredis](https://github.com/laixintao/iredis)
  \- Featureful Redis CLI client with syntax highlight and completions.
- [kubectx](https://github.com/ahmetb/kubectx)
  \- Switch between Kubernetes contexts (clusters) and namespaces easily.
- [kubetail](https://github.com/johanhaleby/kubetail)
  \- Aggregate logs from multiple Kubernetes pods.
- [lazydocker](https://github.com/jesseduffield/lazydocker)
  \- CLI dashboard for Docker and Docker Compose.
- [lychee](https://github.com/lycheeverse/lychee)
  \- A fast and featureful link checker.
- [Midnight Commander (mc)](https://midnight-commander.org/) - The best file manager.
- [mosh](https://mosh.org/) - Like `ssh`, but with local echo and roaming. Good for poor connections.
- [mtr](https://github.com/traviscross/mtr) - Better than `ping`.
- [ncdu](https://dev.yorhel.nl/ncdu) - Disk usage analyzer.
- [ripgrep](https://github.com/BurntSushi/ripgrep) - Fast file content searcher.
- [rmlint](https://github.com/sahib/rmlint)
  \- Free up disk space (e.g. duplicate files).
- [sd](https://github.com/chmln/sd)
  \- A simpler, more intuitive `sed` replacement.
- [speedtest-cli](https://github.com/sivel/speedtest-cli) - Speedtest from a command line.
- [stern](https://github.com/wercker/stern)
  \- Tail multiple k8s logs (like `kubetail`) but more quickly (and optionally in JSON format).
- [storm](https://github.com/emre/storm)
  \- Manage SSH connections (`.ssh/config`).
- [tealdeer](https://github.com/dbrgn/tealdeer) - A very fast [tldr](https://github.com/tldr-pages/tldr) client.
- [thefuck](https://github.com/nvbn/thefuck) - Correct the previous command.
- [tmux](https://github.com/tmux/tmux) - A terminal multiplexer, more user-friendly than screen.
- [tokei](https://github.com/Aaronepower/tokei) - Count the number of source lines, quickly.
- [topgrade](https://github.com/r-darwish/topgrade)
  \- Upgrade just about everything using one single command.
- [watchexec](https://github.com/watchexec/watchexec) - Execute a command when a path is modified.
- [xh](https://github.com/ducaale/xh)
  \- A HTTPie clone in Rust. Much faster startup time compared to the original.

### GUI tools

I'm not a big fan of GUI, but there are a few good ones I use:

- [PosteRazor](https://posterazor.sourceforge.io/index.php?page=about&lang=english)
  \- Print posters (e.g. large images spanning multiple paper pages)
- [QDirStat](https://github.com/shundhammer/qdirstat) - Analyze disk usage by directory / file type.

Linux Desktop specific:
- [Gestures](https://gitlab.com/cunidev/gestures)
  \- A simple GUI for [libinput-gestures](https://github.com/bulletmark/libinput-gestures).
     Easily assign touchpad multi-touch gestures to arbitrary actions.  Also has a useful wiki.

## Data

Books

- [Designing Data-Intensive Applications](https://www.goodreads.com/book/show/23463279-designing-data-intensive-applications)
  \- Excellent book that acts as a guide to modern data engineering (and distributed systems).
     Explains the basic concepts, as well as theory and practical concerns.  Doesn't get too specific
     regarding the software vendors.  Highly recommended.

Date and time

- [Storing UTC is not a silver bullet (archived)](https://web.archive.org/web/20200615073320/https://codeblog.jonskeet.uk/2019/03/27/storing-utc-is-not-a-silver-bullet/)
  \- Why "just store all times in UTC" is sometimes not the best approach.
- [Your Calendrical Fallacy Is...](https://yourcalendricalfallacyis.com/)
  \- A collection of common timekeeping fallacies.

### Databases

- [Don't Do This (PostgreSQL wiki)](https://wiki.postgresql.org/wiki/Don't_Do_This)
  \- What not to do in Postgres.
- [Jepsen Analyses](http://jepsen.io/analyses)
  \- In-depth analyses of multiple database systems.
- [Lessons learned scaling PostgreSQL database to 1.2bn records/month](https://medium.com/@gajus/lessons-learned-scaling-postgresql-database-to-1-2bn-records-month-edc5449b3067)
  \- Very insightful article.
- [Nested Set Model](https://en.wikipedia.org/wiki/Nested_set_model)
  \- Reasonably efficient solution for storing tree structures in relational databases.
     Aka. MPTT (also see example implementation in Django: https://github.com/django-mptt/django-mptt)
- [PostgreSQL is the worlds' best database](https://www.2ndquadrant.com/en/blog/postgresql-is-the-worlds-best-database/)
  \- Arguments for PostgreSQL.
  - [10 Things I Hate About PostgreSQL](https://medium.com/@rbranson/10-things-i-hate-about-postgresql-20dbab8c2791)
    \- A rebuttal to the above, listing shortcomings of Postgres.
- [Readings in Database Systems (commonly known as the "Red Book")](http://www.redbook.io/)
  \- A short book about databases, with lots of references ("readings").

## Design and Web

- [4 Rules for Intuitive UX](https://learnui.design/blog/4-rules-intuitive-ux.html)
  \- Good advice for designing UI, with examples and anti-examples.
- [A JavaScript-Free Frontend](https://web.archive.org/web/20190826003421/https://dev.to/winduptoy/a-javascript-free-frontend-2d3e)
  \- You can do without JavaScript (Archived version).
- [Brutalist Web Design](https://www.brutalist-web.design/)
  \- A set of very reasonable guidelines for designing websites.
- [HTTP headers for the responsible developer](https://www.twilio.com/blog/a-http-headers-for-the-responsible-developer)
  \- Good practices for HTTP headers.
- [Laws of UX](https://lawsofux.com/)
  \- Collection of principles to consider while designing user interfaces.
- [My current HTML boilerplate (April 9, 2021)](https://www.matuzo.at/blog/html-boilerplate/)
  \- A useful HTML boilerplate with in-depth explanations.
- [Opting your Website out of Google's FLoC Network](https://paramdeo.com/blog/opting-your-website-out-of-googles-floc-network)
  \- How to opt your website out of the newest Google tracking mechanism.

## Distributed Systems and Cloud Computing

- [Complexity Explained](https://complexityexplained.github.io/)
  \- Complexity science fundamentals, good to keep in mind when dealing with complex systems.
- [Nines are not enough: meaningful metrics for clouds](https://blog.acolyer.org/2019/06/19/nines-are-not-enough/)
  \- Explains the relationships between SLA, SLI and SLO and how to approach defining them.

Also see the [Data](#data) section.

## Docker

- [Broken by default: why you should avoid most Dockerfile examples](https://pythonspeed.com/articles/dockerizing-python-is-hard/)
  \- Why most `Dockerfile` examples are broken.
- [Intro Guide to Dockerfile Best Practices](https://blog.docker.com/2019/07/intro-guide-to-dockerfile-best-practices/)
  \- Good recommendations for `Dockerfiles`.

## Eye Candy

### Fonts

Programming fonts I found the most eye-pleasing and readable.

- [Hack](https://sourcefoundry.org/hack/)
  \- My font of choice. Very easy on the eyes, and very unambiguous.

### Themes

- [Adapta-gtk-theme](https://github.com/adapta-project/adapta-gtk-theme)
  \- GTK / desktop theme I use. Works great with [Cinnamon](https://github.com/linuxmint/Cinnamon).

## git

- [--force considered harmful; understanding git's --force-with-lease](https://blog.developer.atlassian.com/force-with-lease/)
  \- Why `git push --force-with-lease` is better than `git push --force`
- [delta](https://github.com/dandavison/delta)
  \- A great-looking and featureful CLI git diff viewer.
- [Git in a Nutshell](http://www.aosabook.org/en/git.html)
  \- Overview of how git is implemented.
- [git-quick-stats](https://github.com/arzzen/git-quick-stats)
  \- Get simple statistics for your repo.
- [Little Things I Like to Do with Git](https://csswizardry.com/2017/05/little-things-i-like-to-do-with-git/)
  \- A few useful tips.

### git help

- [git-flight-rules](https://github.com/k88hudson/git-flight-rules)
  \- "Lessons learned" guide to git.
- [Oh shit, git!](http://ohshitgit.com/)
  \- How to revert common git mess-ups.

## Go

- [The Zen of Go](https://dave.cheney.net/2020/02/23/the-zen-of-go)
  \- Go is Go.  A few pointers for idiomatic Go code.

## Hardware and CPUs

- [A fast alternative to the modulo reduction](https://lemire.me/blog/2016/06/27/a-fast-alternative-to-the-modulo-reduction/)
  \- A clever alternative to modulo for spreading out values across a fixed-sized array, like in a hashmap.
- [Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law)
  \- Useful thing to know regarding threading and parallelization.
- [Branch prediction](https://danluu.com/branch-prediction/)
  \- Quick intro to CPU branch prediction.
- [Branch Prediction - Fundamentals Every Programmer Need Not Know](http://www.mycpu.org/branch-prediction-basics/)
  \- Basics and rationale for CPU branch prediction.
- [Common Systems Programming Optimizations & Tricks](https://paulcavallaro.com/blog/common-systems-programming-optimizations-tricks/)
  \- A few low-level tricks.
- [Computer Latency at a Human Scale](https://web.archive.org/web/20200225202909/https://www.prowesscorp.com/computer-latency-at-a-human-scale/)
  \- Latency with human-relatable scales.
- [Floating Point Visually Explained](http://fabiensanglard.net/floating_point_visually_explained/)
  \- The best explanation I've ever seen.
- [Gallery of Processor Cache Effects](https://igoro.com/archive/gallery-of-processor-cache-effects/)
  \- Concise examples showing how cache affects code run time, with good explanations.
- [How does your programming language handle “minus zero” (-0.0)?](https://lemire.me/blog/2021/03/04/how-does-your-programming-language-handle-minus-zero-0-0/)
  \- For numerical programming, it's good to be aware of `-0.0` handling.
- [How to Quantify Scalability](http://www.perfdynamics.com/Manifesto/USLscalability.html)
  \- Some theory, tips and useful models for quantifying systems scalability.
- [How x86_64 addresses memory](https://blog.yossarian.net/2020/06/13/How-x86_64-addresses-memory)
  \- Memory addressing on this platform is quite complicated.
- [Latency Numbers Every Programmer Should Know](https://gist.github.com/GLMeece/b00c9c97a06a957af7426b1be5bc8be6)
  \- Know your latencies.
- [Modern Microprocessors - A 90-Minute Guide!](http://www.lighterra.com/papers/modernmicroprocessors/)
  \- Exceptionally good article on how modern CPUs work. This explains why a lot of low-level
  optimizations work.
- [Performance speed limits](https://travisdowns.github.io/blog/2019/06/11/speed-limits.html)
  \- Super-low-level details of how fast can a CPU execute code.
- [The Fallacy of Premature Optimization](https://ubiquity.acm.org/article.cfm?id=1513451)
  \- Avoiding "premature optimization" doesn't mean we shouldn't optimize at all.
     Thinking about performance early on is important.
- [The microarchitecture of Intel, AMD and VIA CPUs. An optimization guide for assembly programmers and compiler makers](https://www.agner.org/optimize/microarchitecture.pdf)
  \- (PDF) Very in-depth description of inner workings, ins and outs of various CPUs.
- [What Every Programmer Should Know About Memory](https://akkadia.org/drepper/cpumemory.pdf)
  \- (PDF) An in-depth paper on computer memory from (mainly) programming perspective.
- ["What The Hardware Does" is not What Your Program Does: Uninitialized Memory](https://www.ralfj.de/blog/2019/07/14/uninit.html)
  \- Words of warning not to forget the "abstract machine" that programming languages model.

Latency visualized:

[![](https://camo.githubusercontent.com/77f72259e1eb58596b564d1ad823af1853bc60a3/687474703a2f2f692e696d6775722e636f6d2f6b307431652e706e67)](https://gist.github.com/GLMeece/b00c9c97a06a957af7426b1be5bc8be6)

Precision of IEEE 754 Floating Point Values (credit: [Wikipedia](https://en.wikipedia.org/wiki/IEEE_754)):

[![](https://upload.wikimedia.org/wikipedia/commons/3/3f/IEEE754.png)](https://en.wikipedia.org/wiki/IEEE_754#Basic_and_interchange_formats)

## Kubernetes

- [An Illustrated Guide To Kubernetes Networking](https://speakerdeck.com/thockin/illustrated-guide-to-kubernetes-networking)
  \- Slides explaining inner workings of K8S networking.
- [CNCF Cloud Native Interactive Landscape](https://landscape.cncf.io/)
  \- A map grouping all the current and emerging "cloud native" technologies
     (mostly related to Kubernetes).
  - [Cloud Native Trail Map](https://raw.githubusercontent.com/cncf/trailmap/master/CNCF_TrailMap_latest.png)
    \- The migration path to "cloud native".
- [k3s](https://k3s.io/)
  \- Lightweight Kubernetes distribution.
- [Kubernetes Failure Stories](https://k8s.af/)
  \- Learn from other people's mistakes.
- [The Distributed System ToolKit: Patterns for Composite Containers](https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns/)
  \- Explains Sidecar, Ambassador and Adapter container patterns.
- [Two reasons Kubernetes is so complex](https://buttondown.email/nelhage/archive/two-reasons-kubernetes-is-so-complex/)
  \- The K8S complexity has good reasons behind it.

`kubectl` quick reference:

- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
  \- Handy `kubectl` cheat sheet
  - Also very useful: `kubectl explain` -- see: [kubectl explain — #HeptioProTip](https://blog.heptio.com/kubectl-explain-heptioprotip-ee883992a243)
  - `kubectl api-resources` -- show all object kinds, their short names and API groups
    (empty API group means `v1`).
- API exploration:
  - `kubectl explain pod`
  - `kubectl explain pod.spec.volumes.persistentVolumeClaim` -- explain nested specs/objects
- Authorization:
  - `kubectl auth can-i` -- see: [Authorization Overview (k8s docs)](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
- Generating YAMLs quickly:
  - `kubectl create --dry-run -o yaml` -- see: [kubectl Usage Conventions](https://kubernetes.io/docs/reference/kubectl/conventions/#generators)
- Getting all objects:
  - `kubectl get all [-n NAMESPACE] [-l LABEL=VALUE,LABEL2!=VALUE]`

Recipes / how-tos:

- [Kubernetes Network Policy Recipes](https://github.com/ahmetb/kubernetes-network-policy-recipes)
  \- Copy-paste examples of Network Policies with diagrams illustrating their
     effects.

## Linux

- [The Linux Kernel documentation](https://www.kernel.org/doc/html/latest/)
  \- Comprehensive documentation for the Linux kernel.
  - [The kernel’s command-line parameters](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html)

## Management / dealing with people

Books and Resources:

- [Turn the Ship Around!](https://www.goodreads.com/book/show/16158601-turn-the-ship-around)
  \- Great book on management from a US Navy captain.  Straight to the point,
     down-to-earth and genuinely interesting (it's a true story and there's a nuclear submarine involved).

     Focuses on leader-leader approach to management and patterns to introduce it in an organization.
- [Manager's Playbook](https://github.com/ksindi/managers-playbook)
  \- Heuristics for effective management.

Articles / blog posts:

- [22 Principles for Great Product Managers (archived)](https://web.archive.org/web/20210228211201/https://reeve.blog/blog/principles/)
  \- Do product management right.
- [Commit messages guide](https://github.com/RomuloOliveira/commit-messages-guide)
  \- How to write commit messages well.
- [Deadlines Are Killing Us, And Almost Everything Else I Know About Leadership](https://medium.com/@duncanr/deadlines-are-killing-us-and-almost-everything-else-i-know-about-leadership-7032a5fb12ac)
  \- Good article on deadlines, employee motivation, narcissists and management
     overall.
- [Developer to Manager](https://devtomanager.com/)
  \- Collection of interviews with developers who became managers.
- [Do the Real Thing](https://www.scotthyoung.com/blog/2020/05/04/do-the-real-thing/)
  \- Postulates that in order to achieve success, one should focus on real
     things, not distractions and fake alternatives.
- [Early Evangelists of Agile Engineering Wouldn't Mind Watching It Die](https://builtin.com/software-engineering-perspectives/lean-agile-methodology-software-engineering)
  \- Some well-grounded criticisms of modern "agile".
- [Eliminating the Product Owner Role](https://medium.com/@JoshuaKerievsky/eliminating-the-product-owner-role-be01cabc1f5b)
  \- Argues that the "product owner" role might be spread across a team.
- [Habits of High-Functioning Teams](https://deniseyu.io/2020/05/23/habits-of-high-performing-teams.html)
  \- A few principles and rules for high-performing teams.
- [Hanlon's razor](https://en.wikipedia.org/wiki/Hanlon%27s_razor)
  > never attribute to malice that which is adequately explained by stupidity.
- [How NOT to hire a software engineer](https://tonsky.me/blog/hiring/)
  \- Good advice on what not to focus on during an interview.
- [How to be a manager](https://getweeklyupdate.com/manager-guide)
- [How to Deal with Difficult People on Software Projects](https://people.neilon.software/)
  \- We all know "that one guy"...
- [How to Deliver Constructive Feedback in Difficult Situations](https://medium.com/s/please-advise/the-essential-guide-to-difficult-conversations-41f736e63ccf)
  \- In praise of Nonviolent Communication (NVC) principles.
- [How to Stop Endless Discussions](https://candost.blog/how-to-stop-endless-discussions/)
  \- Glorifies the RFC ("Request For Comments") process.
- [Spotify's Failed #SquadGoals](https://www.jeremiahlee.com/posts/failed-squad-goals/)
  \- Why the "Spotify agile model" doesn't work, and recommendations for not
     repeating the same mistakes.
     > (...) the Spotify model is revealed as a collection of cross-functional
       teams with too much autonomy and a poor management structure.
       Don’t fall for it.
- ['Strong Opinions, Weakly Held' Doesn't Work That Well](https://commoncog.com/blog/strong-opinions-weakly-held-is-bad/)
  \- Make sure to present your opinions with probability and be willing to accept other opinions; allow
     the possibility you might be wrong.
     > The next time you find yourself making a judgment, don't invoke 'strong opinions, weakly held'.
       Instead, ask: "how much are you willing to bet on that?" Doing so will jolt people into the types of thinking you want to encourage.
- [The Framing of the Developer](https://www.svese.de/impact-vs-backlog-frame-in-software-development)
  \- Discusses the "Impact oriented" framing vs "Backlog oriented".
     Advocates that we should ditch the backlog frame; instead focus on impact and
     the delivered value.
- [The XY problem](http://xyproblem.info/)
  \- When asking people for help, tell them about the problem, before mentioning
     the attempted solution.
- [Top 12 Things That Destroy Developer Productivity](https://hackernoon.com/top-12-things-that-destroy-developer-productivity-2ddf0abc190)
- [Unlearning toxic behaviors in a code review culture](https://medium.com/@sandya.sankarram/unlearning-toxic-behaviors-in-a-code-review-culture-b7c295452a3c)
- [Users hate change](https://gist.github.com/sleepyfox/a4d311ffcdc4fd908ec97d1c245e57dc)
  \- Arguments for not changing your product if it works and giving users a choice.
- [What Got You Here Won't Get You There (Book Summary)](https://jamesclear.com/book-summaries/what-got-you-here-wont-get-you-there)
  \- Generic tips for leaders.
- [When your coworker does great work, tell their manager](https://jvns.ca/blog/2020/07/14/when-your-coworker-does-great-work-tell-their-manager/)
  \- There's a lot of work being done that's not being recognized.  This is one way to help your coworkers.
- [Why does it take so long to build software?](https://www.simplethread.com/why-does-it-take-so-long-to-build-software/)
  \- Talks about accidental complexity and rapid growth in volume of software.
- [Why software developers (quite honestly) hate Agile](https://www.objectstyle.com/agile/why-developers-hate-agile)
  \- What went wrong with the agile movement and why
     [Software Craftsmanship approach](https://en.wikipedia.org/wiki/Software_craftsmanship) might be better.
- [Work is Work](https://codahale.com/work-is-work/)
  \- Getting effective in management and getting work done in an organization
     is hard work.  There are some universal principles to follow though.
- [Your Company Culture is Who You Hire, Fire, and Promote](https://www.linkedin.com/pulse/your-companys-culture-who-you-hire-fire-promote-part-1-sepah)
  - Part 2: [Anatomy of an Asshole](https://www.linkedin.com/pulse/your-company-culture-who-you-hire-fire-promote-part-2-sepah)
  - Part 3: [Breaking Bad: Why Good People Become Evil Bosses](https://www.linkedin.com/pulse/breaking-bad-why-good-people-become-evilbosses-dr-cameron-sepah)

Talks:

- [Prioritizing Technical Debt as if Time and Money Matters (video)](https://www.youtube.com/watch?v=fl4aZ2KXBsQ)
  \- Talk about dealing with tech debt in a data-driven way.
- [Pushing through Friction (video)](https://www.youtube.com/watch?v=8bxZuzDKoI0)
  \- A few tips on pushing through "organizational friction", and getting your ideas across
     in a large organization.

Timezone tools:

- [Every Time Zone](https://everytimezone.com/)
  \- A readable time zone overview. Useful for scheduling meetings.

Estimating time:

- [PERT (Program evaluation and review technique)](https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique#Time)
    - Also see: [Three-point estimation](https://en.wikipedia.org/wiki/Three-point_estimation)
  ```
  te = (o + 4m + p) / 6
  sigma_te = (p - o) / 6

  Where:
  * o - optimistic estimate (time)
  * m - most likely estimate
  * p - pessimistic estimate
  * te, sigma_te - expected time and its stdev
  ```

Talking about technical debt with business people

(From Kent Beck's twitter: https://twitter.com/KentBeck/status/1187766114706542593 )

- "Investing in improving structure" over "Paying off technical debt"
- "Resilience & Scaling" over "Technical debt work"
- "Upgrade" over "Refactoring"
- Playing Business cards:
    - Reduce cost (including time cost to market and shipping new features)
    - Protect revenue (including preventing disasters)
    - Increase revenue (selling more, adding new features)

Open Source Programs:

- [Open Source Guides For The Enterprise](https://www.linuxfoundation.org/resources/open-source-guides/)
  \- Resources and guidelines for running an open source program.
- [Producing Open Source Software](https://producingoss.com/)
  \- A book on running open source projects.

## Networking

- [Endlessh](https://github.com/skeeto/endlessh)
  \- SSH tarpit server.
- [Reserved IP addresses](https://en.wikipedia.org/wiki/Reserved_IP_addresses)
  \- List of reserved and special purpose addresses (Wikipedia).

  Private IPv4 network ranges:

  ```
  10.0.0.0/8     : 10.0.0.0    - 10.255.255.255
  172.16.0.0/12  : 172.16.0.0  - 172.31.255.255
  192.168.0.0/16 : 192.168.0.0 - 192.168.255.255
  ```

  Other commonly used network ranges:

  ```
  Default Docker bridge network
  172.17.0.0/16  : 172.17.0.1   - 172.17.255.255
  ```

## Privacy

Articles

- [Nothing to hide argument](https://en.wikipedia.org/wiki/Nothing_to_hide_argument)
  \- A Wikipedia article discussing the "I have nothing to hide"
     privacy argument.
- [Three Reasons Why the "Nothing to Hide" Argument is Flawed](https://spreadprivacy.com/three-reasons-why-the-nothing-to-hide-argument-is-flawed/)

Resources

- [Pi-hole](https://pi-hole.net/)
  \- Your custom DNS server, with a lot of features.
     Can run on a Raspberry Pi.
- [privacytools.io](https://www.privacytools.io/)
  \- A grab-bag of resources for the privacy-minded.
- [WireGuard](https://www.wireguard.com/)
  \- The next-generation, fast & easy to use VPN.

## Productivity

- [Busy Person Patterns](https://hillside.net/plop/2006/Papers/Library/PLoP%20Busy%20Person%20Pattern%20v8.pdf)
  \- (PDF) How to be less overwhelmed by the lack of time.
- [Mental models](https://www.defmacro.org/2016/12/22/models.html)
  \- A list of mental models to boost your work
     productivity and efficiency, among other things.
- [Mental Models: The Best Way to Make Intelligent Decisions (109 Models Explained)](https://fs.blog/mental-models/)

## Programming Languages

Resources for no particular language, useful for comparing them.

- [Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code)
  \- Compare language syntax.
- [The Computer Language Benchmarks Game](https://benchmarksgame-team.pages.debian.net/benchmarksgame/)
  \- Which are the fastest? Shows why Rust is so great :)

## Python

Resources related to the Python programming language.

Note that you should only be using Python 3, as
Python 2 will retire (early 2020): [Python 2.7 Countdown](https://pythonclock.org/)

Also see: [Status of Python branches](https://devguide.python.org/#status-of-python-branches)

### Python learning

- [Advanced asyncio: Solving Real-world Production Problems - PyCon 2019 (video)](https://www.youtube.com/watch?v=bckD_GK80oY)
  - [Slides](https://speakerdeck.com/roguelynn/advanced-asyncio-solving-real-world-production-problems)
- [Fluent Python (book)](http://shop.oreilly.com/product/0636920032519.do)
  \- Good book if you know Python basics.
- [How to Make Mistakes in Python](https://web.archive.org/web/20210203141055/https://www.oreilly.com/programming/free/files/how-to-make-mistakes-in-python.pdf)
  \- (PDF). Free book collecting Python antipatterns and common mistakes.
- [I Want A New Duck](https://glyph.twistedmatrix.com/2020/07/new-duck.html)
  \- Advertises `typing.Protocol` (aka. structural typing) as a way to marry
     Python's "duck typing" and mypy type checking.
- [I'm not feeling the async pressure](https://lucumr.pocoo.org/2020/1/1/async-pressure/)
  \- Introduction to the concept of backpressure, as well as advice on how
     to deal with it in Python's `asyncio`.
- [Practical Python (course)](https://github.com/dabeaz-course/practical-python)
  \- Practical Python course, from one of the legendary Python developers,
     David Beazley (`dabeaz`).
- [Python 3 Module of the Week](https://pymotw.com/3/)
  \- Tutorials for standard library modules.
- [Python API Checklist](https://devchecklists.com/python-api-checklist/en/)
  \- Quite a few boxes to tick for good Python APIs.
- [Python Cheatsheet](https://github.com/gto76/python-cheatsheet)
  \- A pretty comprehensive cheatsheet.
- [PyVideo](https://pyvideo.org/)
  \- A huge collection of Python related videos: conference / meetup talks etc.
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)
- [Type hinting (and mypy) - PyCon 2019 (video)](https://www.youtube.com/watch?v=hTrjTAPnA_k)
  - [Blog post (archived)](https://web.archive.org/web/20200605172639/https://www.bernat.tech/the-state-of-type-hints-in-python/)
- [Using Asyncio in Python (book)](https://www.oreilly.com/library/view/using-asyncio-in/9781492075325/)
  \- Worth a read before doing any asyncio.
- [wtfpython](https://github.com/satwikkansal/wtfpython)
  \- A collection of common Python pitfalls and unexpected behaviours.

Python internals and advanced topics:

- [CPython internals (video playlist)](https://www.youtube.com/playlist?list=PLzV58Zm8FuBL6OAv1Yu6AwXZrnsFbbR0S)
  \- Video lectures on Python 2.7 source code. Dated (Python has evolved a bit since 2.7!), but still mostly relevant.
- [How Python does Unicode](https://www.b-list.org/weblog/2017/sep/05/how-python-does-unicode/)
  \- Learn how `str` works under the hood and what does `len(str)` actually return.
- [Inside Python dict](https://github.com/eleweek/inside_python_dict)
- [Inside the New GIL](https://speakerdeck.com/dabeaz/inside-the-new-gil)
  \- Slides from David Beazley on "new" GIL implementation (introduced in 3.2).
- [Modern Dictionaries (video)](https://www.youtube.com/watch?v=p33CVV29OG8)
- [The CPython Bytecode Compiler is Dumb](https://nullprogram.com/blog/2019/02/24/)
  \- A post explaining how dumb (simple) it is (non-optimizing).
- [What I've Learned About Optimizing Python](https://gregoryszorc.com/blog/2019/01/10/what-i've-learned-about-optimizing-python/)
  \- Post listing some performance pitfalls related to CPython implementation.

### Python libraries

- [aio-libs](https://github.com/aio-libs)
  \- A collection of `asyncio` compatible libraries.
- [attrs](https://attrs.readthedocs.io/en/stable/) - Alternative to 3.7's dataclasses.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Pythonic HTML/XML parsing.
- [bleach](https://github.com/mozilla/bleach)
  \- Sanitize untrusted strings so that they are HTML safe.
- [click](https://click.palletsprojects.com/en/7.x/) - Command line argument parser and then some.
- [httpx](https://github.com/encode/httpx)
  \- Requests-inspired HTTP client with both sync and async APIs.
- [irc3](https://github.com/gawel/irc3/) - IRC client based on `asyncio`.
- [janus](https://github.com/aio-libs/janus/) - Queue class that bridges the worlds of `threading` and `asyncio`.
- [Jinja2](http://jinja.pocoo.org/) - The only Python template engine worth your time.
- [Lark](https://github.com/lark-parser/lark) - Fast parsing library.
    Good alternative to [pyparsing](https://github.com/pyparsing/pyparsing/).
- [lxml](https://lxml.de/)
  \- A very fast and featureful (e.g. can use XPath),
     albeit a bit low-level XML and HTML parsing library.
- [NetworkX](https://networkx.github.io/)
  \- [Graph][graph] ("network") manipulation and analysis library.
     Comprehensive yet simple and easy to use.
- [Numba](https://numba.pydata.org/) - JIT compiler for NumPy code. Produces very fast code.
- [pathlib](https://docs.python.org/3/library/pathlib.html) - Excellent standard library module for filesystem path manipulation.
- [Pendulum](https://pendulum.eustace.io/) - A date/time library with nice API.
- [psutil](https://github.com/giampaolo/psutil)
  \- Swiss army knife for process management and system monitoring.
- [pydantic](https://github.com/samuelcolvin/pydantic/)
  \- Pythonic data validation.  Supports `dataclasses` and has a `mypy` plugin.
     Perfect for settings/configs and wherever data validation is required.
- [pydeps](https://github.com/thebjorn/pydeps)
  \- Visualize Python module dependencies.
- [pyjwt](https://github.com/jpadilla/pyjwt)
  \- Work with JSON Web Tokens (JWT).
- [PyPDF2](https://github.com/mstamy2/PyPDF2)
  \- Read and manipulate (e.g. merge) PDF files.
- [PySnooper](https://github.com/cool-RR/pysnooper)
  \- Poor man's debugger for Python.
- [pytest](https://docs.pytest.org/en/latest/) - The only Python test runner worth using these days.
  - Also see [my blog post on basic pytest setup](https://pawroman.gitlab.io/pytest-basic-setup/)
  - [pytest-asyncio](https://github.com/pytest-dev/pytest-asyncio)
    \- Plugin to run asyncio tests easily.
  - [pytest-env](https://github.com/MobileDynasty/pytest-env)
    \- Plugin to set environment variables before any code is imported.
- [quamash](https://github.com/harvimt/quamash)
  \- Use `asyncio` with Qt event loop.
- [requests](https://github.com/psf/requests) - The HTTP library for Python.
- [tqdm](https://github.com/tqdm/tqdm) - Nice progress bar library and command line tool.
- [WebSockets](https://websockets.readthedocs.io/en/stable/) - `asyncio` compatible, no-frills WebSocket client/server.
- [xdoctest](https://github.com/Erotemic/xdoctest)
  \- Better `doctest`, with pytest integration.
  - [Intro video: Developing With Doctests - Using Xdoctest As A Backend](https://www.youtube.com/watch?v=CUjCqOw_oFk)
- [xmltodict](https://github.com/martinblech/xmltodict) - Extract data from XML just like JSON.
- [yarl](https://github.com/aio-libs/yarl)
  \- URL parsing and manipulation library.  Better API (immutable) compared to `furl`.

[graph]: https://en.wikipedia.org/wiki/Graph_(abstract_data_type)

Less known, but very useful things in the standard library:

- [String constants](https://docs.python.org/3/library/string.html#string-constants)
  \- Contains ASCII characters in categorized constants.
- [types.MappingProxyType](https://docs.python.org/3/library/types.html#types.MappingProxyType)
  \- Read-only view into a `dict`, suitable for constants.

### Python news and community

- [PyCoder's Weekly newsletter](https://pycoders.com/)

### Python tools

- [austin](https://github.com/P403n1x87/austin)
  \- Profiler / stack frame sampler, with TUI and optional Web UI.
  - [Deterministic and Statistical Python Profiling](https://p403n1x87.github.io/python/profiling/2019/05/05/python-profiling.html)
    \- Introduces the project and describes Python profiling approaches.
- [IPython](https://ipython.org/) - An enhanced Python shell.
    - [ipdb](https://github.com/gotcha/ipdb) - IPython-enabled debugger.
- [line\_profiler](https://github.com/rkern/line\_profiler) - Profile Python line-by-line.
- [memory\_profiler](https://github.com/pythonprofilers/memory\_profiler)
  \- Profile Python memory usage line-by-line.
- [py-spy](https://github.com/benfred/py-spy)
  \- A low-overhead sampling Python profiler.
- [pyflame](https://github.com/uber/pyflame)
  \- Flame graph profiler based on ptrace (Linux only).
- [scalene](https://github.com/emeryberger/scalene)
  \- A high-performance CPU and memory profiler for Python.

## Rust

### Rust learning

Meta: book of Rust books:

- [The Little Book of Rust Books](https://lborb.github.io/book/)
  \- Aggregates all the Rust related books available freely online.

Quick references / cheatsheets:

- [Rust Language Cheat Sheet](https://cheats.rs/)
- [Rust Memory Container Cheat-sheet](https://github.com/usagi/rust-memory-container-cs)

Get started with Rust:

- [A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)
  \- A very quick intro to Rust.
- [Clear explanation of Rust's module system](http://www.sheshbabu.com/posts/rust-module-system/)
  \- Very good explanation of how modules work.
- [easy_rust](https://github.com/Dhghomon/easy_rust)
  \- Easy Rust. Rust explained using easy English.
     Also available as [a book](https://dhghomon.github.io/easy_rust/Chapter_1.html).
- [idiomatic-rust](https://github.com/mre/idiomatic-rust)
  \- Aggregates articles, talks and repos which deal with concise, idiomatic Rust.
- [Rust by Example](https://doc.rust-lang.org/stable/rust-by-example/)
  \- Rust language showcase, demonstrates the features of the language by example.
- [Rust Cookbook](https://rust-lang-nursery.github.io/rust-cookbook/)
  \- How to accomplish common tasks using idiomatic Rust and libraries.
- [rust-book-summary](https://github.com/psibi/rust-book-summary)
  \- TLDR summary of [The Rust Programming Language Book](https://doc.rust-lang.org/stable/book/).
- [The simplest guide to error handling in Rust](https://kerkour.com/rust-error-handling)
  \- A very concise intro to error handling.
- [Tour of Rust](https://tourofrust.com/)
  \- Similar to "Rust by Example", but more approachable and with more narrative.

Intermediate:

- [A Quick Look at Trait Objects in Rust](https://tratt.net/laurie/blog/entries/a_quick_look_at_trait_objects_in_rust.html)
  \- Explains static vs dynamic dispatch (trait objects).
- [Accurate mental model for Rust's reference types](https://docs.rs/dtolnay/0.0.6/dtolnay/macro._02__reference_types.html)
  \- Explains what `&T` and `&mut T` really are.
- [Allocations in Rust](https://speice.io/2019/02/understanding-allocations-in-rust.html)
  \- Good, in depth intro to how different memory allocation mechanisms
     work in Rust.
- [Cheap tricks for high-performance Rust](https://deterministic.space/high-performance-rust.html)
  \- A few easy tricks around compilation parameters to achieve greater performance.
- [Context-preserving error handling](https://kazlauskas.me/entries/errors)
  \- How to preserve error context while using `thiserror` library.
- [Creating a Rust function that returns a &str or String](https://hermanradtke.com/2015/05/29/creating-a-rust-function-that-returns-string-or-str.html)
  \- Learn to leverage `Cow` to handle string operations.
- [Delete Cargo Integration Tests](https://matklad.github.io/2021/02/27/delete-cargo-integration-tests.html)
  \- A collection of tips towards shorter compile times with tests.
- [Error Handling in Rust](https://blog.burntsushi.net/rust-error-handling/)
  \- Practical guide to handling errors the "raw" Rust way.
- [Generic returns in Rust](https://blog.jcoglan.com/2019/04/22/generic-returns-in-rust/)
  \- On handling `From/Into` traits and how `Iterator::collect()` works.
- [How To Write Fast Rust Code](http://likebike.com/posts/How_To_Write_Fast_Rust_Code.html)
  \- An insightful story of optimization, including tooling recommendations.
- [Join Your Threads](https://matklad.github.io/2019/08/23/join-your-threads.html)
  \- Why ensuring thread join handles are called is important.
- [Learn Rust With Entirely Too Many Linked Lists](https://rust-unofficial.github.io/too-many-lists/index.html)
- [Programming Rust](http://shop.oreilly.com/product/0636920040385.do) - An excellent intermediate-level book on Rust.
- [Rust Design Patterns](https://rust-unofficial.github.io/patterns/)
  \- An interesting collection of Rust patterns, idioms and anti-patterns.
- [Rust: A unique perspective](https://limpet.net/mbrubeck/2019/02/07/rust-a-unique-perspective.html)
  \- An interesting take on mutability, ownership and borrowing in Rust,
     using alternative terminology.
- [Rust: Structuring and handling errors in 2020](https://nick.groenen.me/posts/rust-error-handling/)
  \- Describes good error handling practices using `anyhow` and `thiserror`.
- [rustbattle.net](https://rustbattle.net/)
  \- Rust language quiz.
- [Secure Rust Guidelines](https://anssi-fr.github.io/rust-guide/)
  \- Guide for applications with strong security requirements.
- [The Edition Guide](https://doc.rust-lang.org/nightly/edition-guide/introduction.html)
  \- Learn about Rust 2018 features.
- [The Little Book of Rust Macros](https://danielkeep.github.io/tlborm/book/index.html)
  \- The missing macro tutorial.
- [The Rust Performance Book](https://nnethercote.github.io/perf-book/)
  \- A collection of Rust performance related tips.
- [The Rust Reference](https://doc.rust-lang.org/stable/reference/)
  \- Reference for all language constructs, syntax, types, attributes etc.
- [Working with strings in Rust](https://fasterthanli.me/blog/2020/working-with-strings-in-rust/)
  \- In-depth article on Rust strings, and their ins and outs, with comparison to C.
- [Wrapper Types in Rust: Choosing Your Guarantees](https://manishearth.github.io/blog/2015/05/27/wrapper-types-in-rust-choosing-your-guarantees/)
  \- Overview of pointer, reference, cell and synchronous wrapper types.

Advanced:

- [Crust of Rust: Subtyping and Variance](https://www.youtube.com/watch?v=iVYWDIW71jk)
  \- (Video) Detailed, practical explanation of type/lifetime covariance, contravariance and invariance.
     Also covers the basics of `PhantomData`. All this actually explains a lot of the borrow checker's
     behavior and errors.
- [Crust of Rust: The Drop Check](https://www.youtube.com/watch?v=TJOFSMpJdzg)
  \- (Video) A follow up to the above, covering the drop check, which is closely related to
     `PhantomData` and type variance.
- [min-sized-rust](https://github.com/johnthagen/min-sized-rust)
  \- How to minimize Rust binary size.
- [The Rustonomicon](https://doc.rust-lang.org/nomicon/)
- [Writing an OS in Rust (Second Edition)](https://os.phil-opp.com/)

Evangelism:

- [Rewriting the heart of our sync engine](https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine)
  \- A success story from Dropbox.  Very insightful for rewrites overall, not just about Rust.
- [Rust Companies](https://github.com/omarabid/rust-companies)
  \- List of companies using Rust in production.
- [Rust is for Professionals](https://gregoryszorc.com/blog/2021/04/13/rust-is-for-professionals/)
  > (...) Rust disposes software to a lower defect rate, reduces total development and deployment costs,
  > and is exceptionally satisfying to use.
- [Speed of Rust vs C](https://kornel.ski/rust-c-speed)
  \- Rust has some substantial wins over C.
- [Sustainability with Rust](https://aws.amazon.com/blogs/opensource/sustainability-with-rust/)
  \- Some pros of Rust from the Amazon AWS team.
- [Why Discord is switching from Go to Rust](https://blog.discordapp.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f)
  \- A success story from Discord.
- [Why is Rust the Most Loved Programming Language?](https://matklad.github.io/2020/02/14/why-rust-is-loved.html)
  \- Author's personal
- [Why Rust](https://christine.website/blog/why-rust-2020-02-15)
  \- Compares Rust to Go in a few aspects.
- [Why Rust for safe systems programming](https://msrc-blog.microsoft.com/2019/07/22/why-rust-for-safe-systems-programming/)
  \- Reasons for Rust from Microsoft.
  - Follow up to [We need a safer systems programming language](https://msrc-blog.microsoft.com/2019/07/18/we-need-a-safer-systems-programming-language/)

### Rust libraries

- [assert_cmd](https://github.com/assert-rs/assert_cmd)
  \- Easily test CLI applications.
- [cmd_lib](https://github.com/rust-shell-script/rust_cmd_lib)
  \- Makes running shell commands from Rust very succinct.
- [humantime](https://github.com/tailhook/humantime)
  \- Parse and format human-readable date/times and durations.
- [parking_lot](https://github.com/Amanieu/parking\_lot)
  \- Synchronization primitives faster than standard library.
- [reqwest](https://github.com/seanmonstar/reqwest)
  \- Async HTTP client library, with a blocking mode.  Featureful and well documented.
- [rust-cpython](https://github.com/dgrunwald/rust-cpython)
  \- Expose Rust libraries to Python. Targets stable Rust.
- [serde](https://github.com/serde-rs/serde)
  \- The (de)serialization framework for Rust.  Extremely well done.
- [static_assertions](https://github.com/nvzqz/static-assertions-rs)
  \- Static (compile time) assertions, for API stability and `const` expressions.
- [structopt](https://github.com/TeXitoi/structopt)
  \- Parse CLI args (with env var fallbacks) easily, by defining a struct.
     Reduces CLI args parsing logic to virually zero.
- [wiremock](https://github.com/LukeMathWalker/wiremock-rs)
  \- Excellent HTTP mocking library, e.g. for testing HTTP clients.  Async compatible.

Less known, but very useful things in the standard library:

- [std::clone::Clone::clone_from](https://doc.rust-lang.org/std/clone/trait.Clone.html#method.clone_from)
  \- Perform a (possibly optimized) copy-assignment.
- [std::mem::discriminant](https://doc.rust-lang.org/std/mem/fn.discriminant.html)
  \- Compare enum types statically.

### Rust news and community

- [caniuse.rs](https://caniuse.rs/)
  \- List and search features introduced in each version of Rust (including future ones!).
- [Rust Forge](https://forge.rust-lang.org/)
  \- Rust release dates and many useful links related to the project.
- [Rust Reddit](https://www.reddit.com/r/rust)
- [This Week in Rust](https://this-week-in-rust.org/)
  \- Weekly Rust newsletter, archive available online.

### Rust posts and talks

- [Error Handling Survey](https://blog.yoshuawuyts.com/error-handling-survey/)
  \- In depth overview and discussion of error handling libraries and approaches.
     2019-11-13.
- [How I Wrote a Modern C++ Library in Rust](https://hsivonen.fi/modern-cpp-in-rust/)
- [Is It Time to Rewrite the Operating System in Rust?](https://www.infoq.com/presentations/os-rust)
- [Mocking Time in Async Rust](https://www.ditto.live/blog/mocking-time-in-async-rust)
  \- A neat idea for mocking time in async tests.
- [Optimizations That Aren't, Or Are They?](https://oribenshir.github.io/afternoon_rusting/blog/copy-on-write)
  \- Copy on Write in Rust and C++.
- [Read Rust](https://readrust.net/) - A large collection of Rust related posts.
- [Rust serialization: What's ready for production today?](https://blog.logrocket.com/rust-serialization-whats-ready-for-production-today/)
  \- A quick overview and benchmark of Rust serialization crates.  Published 2020-08-28.
- [Taking Advantage of Auto-Vectorization in Rust](https://nickwilcox.github.io/blog/autovec/)
  \- How to use the type system so the compiler generates SIMD code without
     using any intrinsics manually.
- [The Evolution of a Rust Programmer](https://blog.antoyo.xyz/evolution-rust-programmer)
  \- Tongue-in-cheek post on different Rust programming styles.
- [totally_safe_transmute, line-by-line](https://blog.yossarian.net/2021/03/16/totally_safe_transmute-line-by-line)
  \- A breakdown of a delightful low-level memory access hack, allowing
     transmute without any unsafe code.

Breaking things:

- [Rust in an instant](https://fnordig.de/2020/05/02/rust-in-an-instant/)
  \- A cautionary post about monotonic time and linker symbol shadowing
     (`no_mangle`).

### Rust tools

- [cargo-fuzz](https://github.com/rust-fuzz/cargo-fuzz)
  \- [Fuzzing](https://en.wikipedia.org/wiki/Fuzzing) Rust code.
- [std::dbg](https://doc.rust-lang.org/std/macro.dbg.html)
  \- Standard library debug macro, to replace ad-hoc `println!` debugging.
     Stabilized in 1.32.0.

## Shell

- [Defensive BASH Programming](https://web.archive.org/web/20171211125201/http://www.kfirlavi.com/blog/2012/11/14/defensive-bash-programming/)
  \- Good practices for Bash scripting. (Archived from a defunct blog).
- [gitstatus](https://github.com/romkatv/gitstatus)
  \- Faster `git status` alternative for shells.
- [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
  \- ZSH configuration framework.
- [starship](https://starship.rs/)
  \- Fast, featureful shell prompt. Compatible with many shells.
     The new version (0.45.0+) provides a lot more configuration options compared
     to previous versions.

## Testing

- [Big List of Naughty Strings](https://github.com/minimaxir/big-list-of-naughty-strings)
  \- "list of strings which have a high probability of causing issues when used as user-input data"
- [Building Good Tests](https://salmonmode.github.io/2019/03/29/building-good-tests.html)
  \- Walk through good testing practices. Focused on `pytest`, but also applicable to testing in general.
- [Simple Testing Can Prevent Most Critical Failures (paper + video)](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/yuan)
  \- An Analysis of Production Failures in Distributed Data-Intensive Systems.
     Turns out correct error handling and simple testing is enough to prevent
     most production failures, even in complex distributed systems.
- [TDD, Where Did It All Go Wrong (video)](https://www.youtube.com/watch?v=EZ05e7EMOLM)
  \- A talk on how to do TDD right.
- [Testing Distributed Systems](https://asatarin.github.io/testing-distributed-systems/)
  \- A curated mega-list of resources related to testing distributed systems.
- [Tests that sometimes fail](https://samsaffron.com/archive/2019/05/15/tests-that-sometimes-fail)
  \- Good discussion regarding "flaky" tests, enumerating strategies for dealing
     with them and common causes of flakiness.

### Static Analysis

- [static-analysis](https://github.com/analysis-tools-dev/static-analysis)
  \- "A curated list of static analysis tools for all programming languages,
     config files, build tools, and more."

## Visualization

Links related to data visualization.

- [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/)
  \- A book that is meant "as a guide to making visualizations that accurately
  reflect the data, tell a story, and look professional."
- [matplotlib colormaps](https://bids.github.io/colormap/)
  \- Perceptually uniform colormaps (long merged into Matplotlib).
- [Stop Using Pie-Charts](https://earthly.dev/blog/stop-using-pie-charts/)
  \- Why Pie Charts are unreadable and what do use instead.
