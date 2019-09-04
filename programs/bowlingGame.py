def bowlingGame(a):
	frames = []
	index = 0
	while index < len(a):
		asum = 0
		if a[index] == 10:
			asum += 10 + a[index+1]
			if asum == 20:
				asum += a[index+1]
			frames.append(asum)
			index += 1
		else:
			asum += sum(a[index:index+2])
			if asum == 10:
				asum += a[index+2]
			frames.append(asum)
			index += 2
	return sum(frames)
