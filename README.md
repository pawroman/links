# links

Links to programming related resources I found useful or interesting. A personal "awesome list".

- [Prelude](#prelude)
- [Algorithms](#algorithms)
- [Architecture and Programming Patterns](#architecture-and-programming-patterns)
- [Career Development](#career-development)
- [Code Quality and Good Practices](#code-quality-and-good-practices)
- [Command Line Tools](#command-line-tools)
    - [GUI tools](#gui-tools)
- [Eye Candy](#eye-candy)
    - [Fonts](#fonts)
    - [Themes](#themes)
- [git](#git)
- [Hardware and CPUs](#hardware-and-cpus)
- [Management / dealing with people](#management--dealing-with-people)
- [Programming Languages](#programming-languages)
- [Python](#python)
    - [Python learning](#python-learning)
    - [Python libraries](#python-libraries)
    - [Python news](#python-news)
- [Rust](#rust)
    - [Rust learning](#rust-learning)
    - [Rust talks](#rust-talks)

---

## Prelude

Some of my favourite quotes:

> *"Craftsmanship over Crap"* \
> -- Uncle Bob

> *"… with proper design, the features come cheaply.
> This approach is arduous, but continues to succeed."* \
> -- Dennis Ritchie

> *"Theory is when you know everything but nothing works. \
> Practice is when everything works but no one knows why. \
> In our lab, theory and practice are combined: nothing works and no one knows why."*

---

## Algorithms

Articles:

- [Dijkstra's in Disguise](https://blog.evjang.com/2018/08/dijkstras.html)

Books:

- [Algorithms by Jeff Erickson](http://jeffe.cs.illinois.edu/teaching/algorithms/)
- [The Algorithm Design Manual](http://www.algorist.com/)

Other:

- [Big-O Complexity Cheat Sheet](http://bigocheatsheet.com/)

## Architecture and Programming Patterns

- [Clean Architecture](https://www.goodreads.com/book/show/18043011-clean-architecture)
- [Design Patterns](https://sourcemaking.com/design_patterns) - Describes the classic OO patterns.
- [Game Programming Patterns](http://gameprogrammingpatterns.com/contents.html)
  \- An excellent book on OO patterns found in games. When performance matters.
- [The Architecture of Open Source Applications](http://www.aosabook.org/en/index.html) 

Anti-patterns:

- [Database-as-IPC](https://en.wikipedia.org/wiki/Database-as-IPC)
- [Global Variables Are Bad](http://wiki.c2.com/?GlobalVariablesAreBad)

## Career Development

- [Apprenticeship Patterns](https://www.oreilly.com/library/view/apprenticeship-patterns/9780596806842/)
  \- Problem-solution book for career planning, in praise of
  [software craftsmanship](https://en.wikipedia.org/wiki/Software_craftsmanship).
  Free to read online.

## Code Quality and Good Practices

The Clean trilogy from Robert C. Martin ("Uncle Bob"):

- [Clean Code](https://www.goodreads.com/book/show/3735293-clean-code)
- [The Clean Coder](https://www.goodreads.com/book/show/10284614-the-clean-coder)
- [Clean Architecture](https://www.goodreads.com/book/show/18043011-clean-architecture)

Programming overall:

- [The Pragmatic Programmer](https://pragprog.com/book/tpp/the-pragmatic-programmer) - An absolute classic of a book.
  - [Take-home reference](https://blog.codinghorror.com/a-pragmatic-quick-reference/) - Sums up the book.
  
Principles:

- [Don't Repeat Yourself](https://en.wikipedia.org/wiki/Don't_repeat_yourself)
- [Make It Work, Make It Right, Make It Fast](http://wiki.c2.com/?MakeItWorkMakeItRightMakeItFast)
- [Principle of least astonishment](https://en.wikipedia.org/wiki/Least_astonishment)
- [Rule of three][rule-of-three]

[rule-of-three]: https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)

Principle aggregates / manifestos:

- [Programming Principles](https://github.com/webpro/programming-principles)
- [Software craftsmanship](https://en.wikipedia.org/wiki/Software_craftsmanship)
    - [Manifesto for Software Craftsmanship](http://manifesto.softwarecraftsmanship.org/)

Code quality measures:

- [Cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)

Other:

- [API Evolution the Right Way](https://emptysqua.re/blog/api-evolution-the-right-way/)
- [How To Write Unmaintainable Code](https://github.com/Droogans/unmaintainable-code) - Learn what not to do :)

## Command Line Tools

- [bat](https://github.com/sharkdp/bat) - Syntax and git-aware `cat` clone, with automated paging.
- [DBCLI](https://www.dbcli.com/) - Collection of great CLI database clients,
    e.g. [pgcli](https://www.pgcli.com/), [mycli](https://www.mycli.net/) etc.
- [exa](https://github.com/ogham/exa) - Better than `ls`. Also has a `tree`-like switch (`-T`).
- [fd](https://github.com/sharkdp/fd) - Better than `find`.
- [htop](https://hisham.hm/htop/) - Excellent process viewer.
- [HTTPie](https://httpie.org/) - cURL for humans. Uses Python + requests.
- [hyperfine](https://github.com/sharkdp/hyperfine) - CLI benchmarking tool.
- [Midnight Commander (mc)](https://midnight-commander.org/) - The best file manager.
- [mosh](https://mosh.org/) - like `ssh`, but with local echo and roaming. Good for poor connections.
- [mtr](https://github.com/traviscross/mtr) - Better than `ping`.
- [ncdu](https://dev.yorhel.nl/ncdu) - Disk usage analyzer.
- [ripgrep](https://github.com/BurntSushi/ripgrep) - Fast file content searcher.
- [speedtest-cli](https://github.com/sivel/speedtest-cli) - Speedtest from a command line.
- [tealdeer](https://github.com/dbrgn/tealdeer) - A very fast [tldr](https://github.com/tldr-pages/tldr) client.
- [thefuck](https://github.com/nvbn/thefuck) - Correct the previous command.
- [tmux](https://github.com/tmux/tmux) - A terminal multiplexer, more user-friendly than screen.
- [tokei](https://github.com/Aaronepower/tokei) - Count the number of source lines, quickly.
- [watchexec](https://github.com/watchexec/watchexec) - Execute a command when a path is modified.

### GUI tools

I'm not a big fan of GUI, but there are a few good ones I use:

- [QDirStat](https://github.com/shundhammer/qdirstat) - Analyze disk usage by directory / file type.

## Eye Candy

### Fonts

Programming fonts I found the most eye-pleasing and readable.

- [Hack](https://sourcefoundry.org/hack/) - My font of choice. Very easy on the eyes, and very unambiguous.

### Themes

- [Adapta-gtk-theme](https://github.com/adapta-project/adapta-gtk-theme)
    \- GTK / desktop theme I use. Works great with [Cinnamon](https://github.com/linuxmint/Cinnamon).

## git

- [Git in a Nutshell](http://www.aosabook.org/en/git.html) - Overview of how git is implemented.
- [Oh shit, git!](http://ohshitgit.com/) - How to revert common git mess-ups.

## Hardware and CPUs

- [Floating Point Visually Explained](http://fabiensanglard.net/floating_point_visually_explained/)
  \- The best explanation I've ever seen.
- [Modern Microprocessors - A 90-Minute Guide!](http://www.lighterra.com/papers/modernmicroprocessors/)
  \- Exceptionally good article on how modern CPUs work. This explains why a lot of low-level
  optimizations work.

## Management / dealing with people

- [Every Time Zone](https://everytimezone.com/) - A readable time zone overview. Useful for scheduling meetings.
- [How to Deal with Difficult People on Software Projects](https://people.neilon.software/) - We all know "that one guy"...
- [How to be a manager](https://getweeklyupdate.com/manager-guide)
- [Unlearning toxic behaviors in a code review culture](https://medium.freecodecamp.org/unlearning-toxic-behaviors-in-a-code-review-culture-b7c295452a3c)

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

### Python learning

- [Fluent Python](http://shop.oreilly.com/product/0636920032519.do) - Good book if you know Python basics.
- [How to Make Mistakes in Python](https://www.oreilly.com/programming/free/files/how-to-make-mistakes-in-python.pdf)
  \- Book collecting Python antipatterns and common mistakes. Free PDF.
- [PyVideo](https://pyvideo.org/) - A huge collection of Python related videos: conference / meetup talks etc.
- [Python API Checklist](https://devchecklists.com/python-api-checklist/)
- [Python 3 Module of the Week](https://pymotw.com/3/) - Tutorials for standard library modules.
- [The Hitchhiker's Guide to Python](https://docs.python-guide.org/)
- [Using Asyncio in Python 3](https://www.oreilly.com/library/view/using-asyncio-in/9781491999691/) - Worth a read before doing any asyncio.

Python internals:

- [CPython internals](http://pgbovine.net/cpython-internals.htm)
  \- Video lectures on Python 2.7 source code. Dated, but still mostly relevant.
- [Inside Python dict](https://just-taking-a-ride.com/inside_python_dict/chapter1.html)
- [Modern Dictionaries (video)](https://www.youtube.com/watch?v=p33CVV29OG8)


### Python libraries

- [attrs](https://attrs.readthedocs.io/en/stable/) - Alternative to 3.7's dataclasses.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Pythonic HTML/XML parsing.
- [click](https://click.palletsprojects.com/en/7.x/) - Command line argument parser and then some.
- [Jinja2](http://jinja.pocoo.org/) - The only Python template engine worth your time.
- [Numba](https://numba.pydata.org/) - JIT compiler for NumPy code. Produces very fast code.
- [pathlib](https://docs.python.org/3/library/pathlib.html) - Excellent standard library module for filesystem path manipulation.
- [Pendulum](https://pendulum.eustace.io/) - A date/time library with nice API.
- [pytest](https://docs.pytest.org/en/latest/) - The only Python test runner worth using these days.
  - Also see [my blog post on basic pytest setup](https://iwwn.pl/post/pytest-basic-setup/)
- [requests](http://docs.python-requests.org/en/master/) - The HTTP library for Python.
- [tqdm](https://github.com/tqdm/tqdm) - Nice progress bar library and command line tool.
- [WebSockets](https://websockets.readthedocs.io/en/stable/) - `asyncio` compatible, no-frills WebSocket client/server.
- [xmltodict](https://github.com/martinblech/xmltodict) - Extract data from XML just like JSON.

### Python news

- [PyCoder's Weekly newsletter](https://pycoders.com/)

### Python tools

- [IPython](https://ipython.org/) - An enhanced Python shell.
- [line\_profiler](https://github.com/rkern/line\_profiler) - Profile Python line-by-line.

## Rust

### Rust learning

- [Programming Rust](http://shop.oreilly.com/product/0636920040385.do) - An excellent intermediate-level book on Rust.
- [The Little Book of Rust Macros](https://danielkeep.github.io/tlborm/book/index.html) - The missing macro tutorial.

Advanced:

- [The Rustonomicon](https://doc.rust-lang.org/nomicon/)
- [Writing an OS in Rust (Second Edition)](https://os.phil-opp.com/)

### Rust talks

- [Is It Time to Rewrite the Operating System in Rust?](https://www.infoq.com/presentations/os-rust)
