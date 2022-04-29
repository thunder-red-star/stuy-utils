# Breaking Changes
In version 0.0.4 (ThunderRedStar's fork of the original [0.0.3](https://github.com/achen318/stuy-utils)) of this library, the following breaking changes were introduced:
* All dates are stored as tsv files instead of csv files.
* There are multiple bell schedules (including special ones, like homeroom, conference, etc).
* **All bell schedules include a "before school" period.**
* Passing periods (between two periods) are included, to skip them in get_next_class() use `skip_passing=True`.