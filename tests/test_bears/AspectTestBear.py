from coalib.bearlib.aspects import get as get_aspect, AspectList
from coalib.bears.LocalBear import LocalBear
from coalib.results.Result import Result
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY


class AspectTestBear(LocalBear, aspects={
    'detect': [get_aspect('coalaCorrect')]
}):
    LANGUAGES = {'python'}
    LICENSE = 'AGPL-3.0'

    def run(self, filename, file, aspects: AspectList=None, config: str=''):
        """
        Bear that have aspect.

        :param config: An optional dummy config file.
        """
        print('tests')
        yield Result.from_values(
            origin=self,
            message='The correct way to write coala is `coala`',
            severity=RESULT_SEVERITY.INFO,
            file=filename,
            aspect=get_aspect('coalaCorrect'))
