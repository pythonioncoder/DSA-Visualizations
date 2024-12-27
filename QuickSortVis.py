import matplotlib.pyplot as plt
import numpy as np
import pygame
import time

pygame.mixer.init()


def play_tone(frequency, duration):
	sample_rate = 44100  # Hertz
	n_samples = int(sample_rate * duration)

	# Create a sine wave
	t = np.linspace(0, duration, n_samples, False)
	wave = 0.5 * np.sin(2 * np.pi * frequency * t)

	# Convert to 16-bit audio data
	wave = (wave * 32767).astype(np.int16)

	# Duplicate for stereo if needed
	wave = np.column_stack((wave, wave))  # Convert to 2 channels (stereo)

	# Make and play sound
	sound = pygame.sndarray.make_sound(wave)
	sound.play(-1)
	time.sleep(duration)
	sound.stop()


class Vis:
	def __init__(self, a=100, barcol='white'):
		self.amount = a
		self.barcol = barcol
		self.lst = []
		self.x = np.arange(0, self.amount, 1)
		self.highlights = np.full(self.amount, barcol)
		self.end = False

		vals = np.arange(self.amount)
		for i in vals:
			x = np.random.randint(0, len(vals))
			self.lst.append(vals[x])
			vals = np.delete(vals, x)
		self.lst = np.array(self.lst)

	def display(self):
		plt.clf()
		plt.gcf().set_facecolor('black')
		plt.bar(self.x, self.lst, color=self.highlights)
		plt.axis('off')
		plt.pause(0.0001)
		if self.end:
			plt.close()
			return


def _quick_sort(current: Vis, lo, hi):
	unsorted = current.lst[lo:hi]

	if len(unsorted) < 2:
		return unsorted

	pivot = np.median([unsorted[0], unsorted[len(unsorted)//2], unsorted[-1]])
	if pivot == unsorted[0]:
		pivot_index = 0
	elif pivot == unsorted[-1]:
		pivot_index = len(unsorted)-1
	else:
		pivot_index = len(unsorted)//2
	i = -1
	j = len(unsorted)
	while True:
		i += 1
		j -= 1
		while unsorted[i] < pivot:
			i += 1
		while unsorted[j] > pivot:
			j -= 1

		if j <= i:
			break

		current.highlights[lo+i], current.highlights[lo+j], current.highlights[lo+pivot_index] = 'green', 'green', 'red'
		current.display()

		temp = unsorted[i]
		unsorted[i] = unsorted[j]
		unsorted[j] = temp

		current.display()
		play_tone((unsorted[i] + unsorted[j]) * 50 / 2 + 100, 0.01)
		current.highlights[lo+i], current.highlights[lo+j], current.highlights[lo+pivot_index] = current.barcol, current.barcol, current.barcol

	res = _quick_sort(current, lo, lo+i) + _quick_sort(current, lo+i, hi)

	if lo == 0 and hi == len(current.lst):
		for i in range(len(current.lst)):
			current.highlights[i] = 'green'
			current.display()
			play_tone(current.lst[i]*50+100, 0.01)
		current.end = True
		current.display()

	return res


def quick_sort(current: Vis):
	return _quick_sort(current, 0, len(current.lst))


if __name__ == '__main__':
	my_vis = Vis()
	quick_sort(my_vis)
