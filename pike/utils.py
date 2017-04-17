import os.path
import shutil
from string import Template


PIKE_DIR = os.path.dirname(__file__)
SAMPLES_DIR = os.path.join(PIKE_DIR, 'samples')

def sample_path(sample):
    path = os.path.join(SAMPLES_DIR, sample)
    return os.path.realpath(path)

def copy_sample(sample, target):
    source = os.path.join(SAMPLES_DIR, sample)
    shutil.copy(source, target)

def render_sample(sample, **kwargs):
    source = os.path.join(SAMPLES_DIR, sample)
    with open(source, 'r') as f:
        text = f.read()
    template = Template(text)
    return template.substitute(kwargs)
