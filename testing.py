import unirest

results = []
threads = []

def showData():
	for m in results:
		print m

def processResults(response):
	results.append(response.raw_body)

def main():
	thread = unirest.get(
		"http://api.randomuser.me/",
		callback=processResults)
	threads.append(thread)

for i in range(0, 15):
	main()
print "LISTOO"

for t in threads:
	print "hilo"
	t.join()

print len(results)