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
	def __init__(self, a=50, barcol='white'):
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


def selection_sort(current: Vis):
	unsorted = current.lst
	for i in range(len(unsorted) - 1):
		min_index = i
		for j in range(i + 1, len(unsorted)):
			if unsorted[j] < unsorted[min_index]:
				min_index = j
			current.highlights[min_index] = 'red'
			current.highlights[j] = 'green'
			current.display()
			play_tone(unsorted[j]*50+100, 0.01)
			current.highlights[min_index], current.highlights[j] = current.barcol, current.barcol

		if i != min_index:
			temp = unsorted[i]
			unsorted[i] = unsorted[min_index]
			unsorted[min_index] = temp

	for i in range(len(unsorted)):
		current.highlights[i] = 'green'
		current.display()
		play_tone(unsorted[i]*50+100, 0.01)

	current.end = True
	current.display()

	return unsorted


if __name__ == '__main__':
	my_vis = Vis()
	selection_sort(my_vis)
