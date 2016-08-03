from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from webapp.models import db
from webapp.app_factory import create_app


def run_migrations():

    # manager = Manager(app)

    app = create_app(database=db)

    Migrate(app, db)

    manager = Manager(app)

    # manager = Manager(create_app)
    manager.add_command('db', MigrateCommand)
    # manager.add_option('--dbname', dest='db_name', required=False)
    # manager.add_option('--dbuser', dest='db_username', required=False)
    # manager.add_option('--dbpass', dest='db_password', required=False)
    # manager.add_option('--dbserver', dest='db_server', required=False)
    # manager.add_option('--config', dest='extra_config', required=False)
    # manager.add_option('--database', dest='database', default=db)
    # manager.add_option('--initialize-bps', dest='initialize_blueprints',
    #                    default=True)
    # manager.add_option('--callback', dest='callback', default=Migrate)
    # manager.add_option('--callback-args', dest='callback_args',
    #                    default=[db])

    manager.run()

if __name__ == '__main__':
    print "in run migration"
    run_migrations()
