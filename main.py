from dolly_zoom import *
import cv2
import os
import imageio
import matplotlib.pyplot as plt
from IPython.display import Image

def rotY(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def generate_gif():
    n_frames = 30
    if not os.path.isdir("frames"):
        os.mkdir("frames")
    fstr = "frames/%d.png"
    for i,theta in enumerate(np.arange(0,2*np.pi,2*np.pi/n_frames)):
        fname = fstr % i
        renderCube(f=15, t=(0,0,3), R=rotY(theta))
        plt.savefig(fname)
        plt.close()

    with imageio.get_writer("cube.gif", mode='I', loop=0) as writer:
        for i in range(n_frames):
            frame = plt.imread(fstr % i)
            if frame.dtype == np.float32:
                frame = (frame * 255).astype(np.uint8)
            writer.append_data(frame)
            os.remove(fstr%i)
            
    os.rmdir("frames")

generate_gif()