from coalib.bearlib.aspects import Root, Taste


@Root.subaspect
class Formatting:
    """
    This aspect describe how your source code is formatted. The Formatting 
    aspect should not have modify the program behaviour.
    """


@Formatting.subaspect
class Line:
    """
    Everything in a line.
    """

@Formatting.subaspect
class Naming:
    """
    How to name a thing like filename, variable name, or class name.
    """

@Formatting.subaspect
class AlignParameters:
    """
    Here we check if the parameters on a multi-line method call or definition 
    are aligned.
    """
    class docs:
        example = """# bad (double indent)
def send_mail(source)
  Mailer.deliver(
      to: 'bob@example.com',
      from: 'us@example.com',
      subject: 'Important message',
      body: source.text)
end"""
        example_language = 'Ruby'
        importance_reason = """
        test
        """
        fix_suggestions = """Align multiline parameters as deep as the opening
        indent"""


@Line.subaspect
class LineLength:
    """
    Some projects force to use colons in the commit message shortlog
    (first line).
    """
    class docs:
        example = """
a reaaalllyyyy looooooooooooooooooooooooongggggggg liineeeeeeeeeeeeeeeeesss of cooooodeeee
        """
        example_language = 'All'
        importance_reason = """
        test dad addsadasdd
        """
        fix_suggestions = """
        Align multiline parameters as deep as the opening
        indent
        """

    max_line_length = Taste[int](
        'Max length of a single line',
        (79, 80, 100, 120), default=79)


@Line.subaspect
class Indentation:
    """
    A defintion
    """
    class docs:
        example = """
        # bad, inconsistent indentation width
        int a = 1;
        if (a < 5) {
            println(a);
          a += 5;
        }"""
        example_language = 'C'
        importance_reason = """
        A proper and uniform indentation make reading your code easier.        
        """
        fix_suggestions = """
        Align indentation in your code.
        """

    indentation_width = Taste[int](
        'Width of indentation.',
        (2, 3, 4, 8), default=4)
    indentation_type = Taste[str](
        'Type of indentation',
        ('tab', 'space'), default='space')


@Naming.subaspect
class VariableNaming:
    """
    How to name a variable correctly
    """
    class docs:
        example = """
        # bad variable name
        aCamelCaseVariable = 'doesn't comply to code style'
        """
        example_language = 'Python'
        importance_reason = """
        Uniform variable naming make reading code more predictable.
        """
        fix_suggestions = """
        User proper capitalization or special character.
        """

    naming_convention = Taste[str](
        'Naming convention',
        ('underscore', 'camel_case', 'pascal_case'),
        default='underscore')