import os.path
import shutil

from jinja2 import Environment, FileSystemLoader


PIKE_DIR = os.path.dirname(__file__)
SAMPLES_DIR = os.path.join(PIKE_DIR, 'samples')

def sample_path(sample):
    path = os.path.join(SAMPLES_DIR, sample)
    return os.path.realpath(path)

def copy_sample(sample, target):
    source = os.path.join(SAMPLES_DIR, sample)
    shutil.copy(source, target)

def render_sample(template, **kwargs):
    env = Environment(loader=FileSystemLoader(SAMPLES_DIR))
    template = env.get_template(template)
    return template.render(**kwargs)
