# 01. The Python Interpreter

---

## The Python Program

The Python interpreter program is run as `python` and includes both the interpreter itself and the **Python compiler**, which is implicitly invoked, as and if needed, on imported modules.

### Environment Variables

Besides PATH, other environment variables affect the `python` program. Some environment variables have the same effects as options passed to `python` on the command line, as we show in the next section. Several environment variables provide settings not available via command-line options. The following list covers just the basics of a few frequently used ones; for all details, see the [online docs](https://docs.python.org/3/using/cmdline.html#environment-variables).

### Command-Line Syntax and Options

The Python interpreter command-line syntax can be summarized as follows:

```bash
[path]python {options} [-c command | -m module | file | -] {args}
```

Brackets (**[ ]**) enclose what’s optional, braces (**{ }**) enclose items of which zero or more may be present, and bars (**|**) mean a choice among alternatives. Python uses a slash (**/**) for file paths, as in Unix.

## Running Python Programs

Running a Python script at a command line can be as simple as:

```
$ python hello.py
Hello World
```

The filename of the script can be any absolute or relative file path, and need not have any specific extension (though it is conventional to use a *.py* extension).