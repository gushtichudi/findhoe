import sys


class Kind:
    ok = 1
    info = 2
    warning = 3
    error = 4


class Formatting:
    def __init__(self):
        self.end = "\x1b[0m"

    def construct_escape(self, coloring, color: int, bold: bool, under: bool) -> str:
        match coloring:
            case "background":
                if color > 7:
                    raise ValueError("There are no more than 7 colors.")

                if bold:
                    return f"\x1b[1;4{color}m"
                elif under:
                    return f"\x1b[2;4{color}m"
                else:
                    return f"\x1b[0;4{color}m"

            case "foreground":
                if color > 7:
                    raise ValueError("There are no more than 7 colors.")

                if bold:
                    return f"\x1b[1;3{color}m"
                elif under:
                    return f"\x1b[2;3{color}m"
                else:
                    return f"\x1b[0;3{color}m"

            case _:
                pass

    def message(self, kind: Kind, msg: str, die_on_error: bool = False):
        match kind:
            case Kind.ok:
                grn = self.construct_escape("foreground", 2, False, False)
                sys.stdout.write(f"[ OK ]:: {grn}{msg}{self.end}\n")
            case Kind.info:
                blu = self.construct_escape("foreground", 4, False, False)
                sys.stdout.write(f"[INFO]:: {blu}{msg}{self.end}\n")
            case Kind.warning:
                yel = self.construct_escape("foreground", 3, False, False)
                sys.stdout.write(f"[WARN]:: {yel}{msg}{self.end}\n")
            case Kind.error:
                red = self.construct_escape("foreground", 1, False, False)
                sys.stderr.write(f"[FAIL]:: {red}{msg}{self.end}\n")
                if die_on_error:
                    exit(1)
            case _:
                raise ValueError("That is not a valid kind.")
