#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home_for_animals.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

"""
docker run -it --network=traefik \
--label "traefik.enable=true" \
--label "traefik.http.routers.home_for_animals.rule=Host(\'api.zq_strayanimals.ziqiang.net.cn\')" \
--label "traefik.http.routers.home_for_animals.entrypoints=websecure" \
--label "traefik.http.services.home_for_animals.loadbalancer.server.port=8083" \
--name zq_strayanimals home_for_cute_animals
"""