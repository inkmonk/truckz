from webapp.app_factory import create_app
from webapp.models import db, User, Role, TruckOwner
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


def seed_truck_owners(n=50):
    for u in User.all(reverse=True, limit=n):
        u.truck_owner = TruckOwner.new(user_id=u.id, company_name=fake.name(), city=fake.city())
    db.session.commit()


if __name__ == '__main__':
    app = create_app(db)
    with app.test_request_context():
        create_admin_role()
        create_admin_user()
        seed_users(100)
        seed_truck_owners(50)
