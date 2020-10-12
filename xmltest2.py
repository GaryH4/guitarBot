from xml.dom import minidom
import enhancedminidom

queue = [[0]]

filename="/home/pi/servo/lg-202876558.xml"
scoreFile = minidom.parse(filename)
score = scoreFile.documentElement
measures=score.getElementsByTagName("measure")
for measure in measures:
    measure_list = []
    measure_list.append(int(measure.getAttribute("number")))
    notes = measure.getElementsByTagName("note")
    for note in notes:
        note_list = []
        if(note.getElementsByTagName("rest")!=[]):
            note_list.append("rest")
        else:
            step = note.getElementsByTagName("step")[0].childNodes[0].data
            octave = note.getElementsByTagName("octave")[0].childNodes[0].data
            note_list.append(step+octave)
            type = note.getElementsByTagName("type")[0].childNodes[0].data
        duration = int(note.getElementsByTagName("duration")[0].childNodes[0].data)
        note_list.append(duration)
        if(type!=[]):
            note_list.append(type)
        measure_list.append(note_list)
    queue.append(measure_list)

while(queue):
    print(queue.pop(0))


    
