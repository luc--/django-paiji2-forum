# Copyright (C) 2015 Louis-Guillaume DUBOIS
#
# This file is part of paiji2-forum
#
# paiji2-forum is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# paiji2-forum is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.apps import AppConfig


class Paiji2_ForumConfig(AppConfig):

    name = 'paiji2_forum'
    verbose_name = 'paiji2 forum'

    def ready(self):
        import update_db
        update_db.update_icons_db()
