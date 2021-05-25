from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import esr21_enrollment_schedule, esr21_fu_schedule

esr21_visit_schedule = VisitSchedule(
    name='esr21_visit_schedule',
    verbose_name='ESR@!',
    offstudy_model='esr21.subjectlocator',
    locator_model='esr21_subject.subjectlocator',
    death_report_model='',
    previous_visit_schedule=None)

esr21_visit_schedule.add_schedule(esr21_enrollment_schedule)
esr21_visit_schedule.add_schedule(esr21_fu_schedule)

site_visit_schedules.register(esr21_visit_schedule)
