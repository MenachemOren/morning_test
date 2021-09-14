import pytest
from pytest_bdd import given, when, then, scenario

# from tests.objects import Objects
from objects import Objects


@scenario('morning.features', 'edit profile')
def test_we_want_to_edit_profile_in_mongo_application():
    """edit profile"""
    pass

@pytest.fixture(scope='function')
def context():
    return {}


@given("there is a user profile")
def step_impl(context):
    context['my_object'] = Objects()


@when("i edit the profile")
def step_impl(context):
    context['my_object'].edit_name("menachem")
    context['my_object'].edit_mail("menachem@mail")
    context['my_object'].edit_interests("baking")
    context['my_object'].update()



@then("the user profile will change")
def step_impl(context):
    mongo_name = context['my_object'].get_mongo_name()
    mongo_mail = context['my_object'].get_mongo_mail()
    mongo_interests = context['my_object'].get_mongo_interests()
    context['my_object'].close_drivers()
    assert(mongo_name == 'menachem')
    assert(mongo_mail == 'mail')
    assert(mongo_interests == 'bake')