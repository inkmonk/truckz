from webapp.app_factory import create_app
from webapp.models import db, User, Role, TruckOperator
from flask_security.utils import encrypt_password
from faker import Factory as FakerFactory

fake = FakerFactory.create()
fake.seed(1234)


def create_admin_role():
    return Role.find_or_create(name="admin")

def create_admin_user():
    u = User.update_or_create(
        name="admin", email="admin@truckz.io",
        password=encrypt_password("password"),
        active=True, keys=["email"])
    u.roles.append(Role.first(name="admin"))
    db.session.commit()


def seed_users(n=10):
    password = encrypt_password("password")
    return User.find_or_create_all([
        dict(name=fake.name(), email=fake.email(),
             password=password, active=True)
        for _ in range(n)], keys=['email'])


def seed_truck_operators(n=5):
	for u in User.all(limit=n):
		u.employing_truck_operator = TruckOperator.new(
			company_name=fake.name(),
			city=fake.city())
	db.session.commit()


if __name__ == '__main__':
    app = create_app(db)
    with app.test_request_context():
        create_admin_role()
        create_admin_user()
        seed_users()
        seed_truck_operators()
