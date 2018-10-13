def exec_summary(labels):
    image_tags = ""
    string = "This image pertains to"
    counter = 0
    for label in labels:
        if(counter==0 or counter==1):
            image_tags = image_tags+" "+label.description+","
            counter+=1
        elif(counter==2):
            image_tags = image_tags+" and "+label.description
            counter+=1
        else:
            break
    image_tags = image_tags+"."
    string = string + image_tags
    return string
