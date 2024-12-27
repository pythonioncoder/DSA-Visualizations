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


def _merge_sort(current: Vis, lo, hi):
	unsorted = current.lst[lo:hi]

	if len(unsorted) < 2:
		return unsorted

	left = _merge_sort(current, lo, lo + round(len(unsorted)/2)).copy()
	right = _merge_sort(current, lo + round(len(unsorted)/2), hi).copy()

	l, r = 0, 0
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			current.lst[lo+l+r] = left[l]
			l += 1
			current.highlights[lo+l+r] = 'green'
			current.display()
			play_tone(left[l-1]*50+100, 0.01)
			current.highlights[lo + l + r] = current.barcol
		else:
			current.lst[lo+l+r] = right[r]
			r += 1
			current.highlights[lo + l + r] = 'green'
			current.display()
			play_tone(right[r-1]*50+100, 0.01)
			current.highlights[lo + l + r] = current.barcol

	if l < len(left):
		for i in range(len(left[l:])):
			current.lst[lo+l+r+i] = left[l+i]
			current.highlights[lo + l + r] = 'green'
			current.display()
			play_tone(left[l+i]*50+100, 0.01)
			current.highlights[lo + l + r] = current.barcol
	elif r < len(right):
		for i in range(len(right[r:])):
			current.lst[lo+l+r+i] = right[r+i]
			current.highlights[lo + l + r] = 'green'
			current.display()
			play_tone(right[r+i]*50+100, 0.01)
			current.highlights[lo + l + r] = current.barcol

	if lo == 0 and hi == len(current.lst):
		for i in range(len(current.lst)):
			current.highlights[i] = 'green'
			current.display()
			play_tone(current.lst[i]*50+100, 0.01)
		current.end = True
		current.display()

	return current.lst[lo:hi]


def merge_sort(current: Vis):
	return _merge_sort(current, 0, len(current.lst))


if __name__ == '__main__':
	my_vis = Vis()
	merge_sort(my_vis)
