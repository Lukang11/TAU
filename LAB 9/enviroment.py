from behave import fixture, use_fixture
from cypress_runner import CypressRunner

@fixture
def cypress_fixture(context):
    context.cypress_runner = CypressRunner()
    context.cypress_runner.install()
    context.cypress_runner.open()
    yield context.cypress_runner
    context.cypress_runner.close()

def before_all(context):
    use_fixture(cypress_fixture, context)
