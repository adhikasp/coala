import coalib.bearlib.aspects

from .meta import aspectclass
from .base import aspectbase, issubaspect, assert_aspect

class aspectlist(list):
    """
    List-derived container to hold aspects.
    """

    def __init__(self, seq=()):
        """
        Initialize a new aspectlist.

        >>> aspectlist([Root.Spelling.coalaCorrect, Root.Spelling.aspectsYEAH])
        [<aspectclass '...coalaCorrect'>, <aspectclass '...aspectsYEAH'>]
        >>> aspectlist(['coalaCorrect', 'aspectsYEAH'])
        [<aspectclass '...coalaCorrect'>, <aspectclass '...aspectsYEAH'>]

        :param seq: A sequence  containing either aspectsclass,
                    aspectsinstance, or string of partial/fully qualifie
                    aspects name
        """
        if all(map((lambda x: isinstance(x, str), seq))):
            super().__init__(map((lambda x: coalib.bearlib.aspects[x]), seq))
        else:
            super().__init__(map(assert_aspect, seq))

    def __contains__(self, aspect):
        for item in self:
            if issubaspect(aspect, item):
                return True
        return False

    def get(self, aspect):
        if isinstance(aspect, str):
            aspect = coalib.bearlib.aspects[aspect]

        if isinstance(aspect, aspectclass):
            return any(map(lambda x: isinstance(aspect, x), self)
        elif isinstance(aspect, aspectbase):
            return any(map(lambda x: aspect is x)), self)

def create_aspects_instance_from_section(aspect_list, language, section):
    aspects_instance = aspectlist()
    for aspect in aspect_list:
        tastes_to_init = dict()
        for taste in aspect.tastes:
            try:
                tastes_to_init[taste] = section[taste]
            except IndexError:
                pass
        aspects_instance.append(aspect(language, **tastes_to_init))
    return aspects_instance
