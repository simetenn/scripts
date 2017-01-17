import os, shutil, sys

#path = "/media/simen/Dragonlord/Media/TV Shows/"
path = "/home/simen/Downloads/"

show = sys.argv[1]
seasons = os.listdir(path + show)


for season in seasons:
    files = os.listdir(path + show + "/" + season)
    s = season.split()[1]
    episode = 1

    for f in files:

        split = f.split("-")
        name = show

        try:
            try:
                try:
                    try:
                        episode = int(split[len(show.split())].split("E")[1])
                    except:
                        episode = int(split[len(show.split())].split("e")[1])
                except:
                    episode = int(split[len(show.split())].split("ep")[1])
            except:
                episode = int(split[len(show.split())].split("x")[1])
        except:
            pass

        print episode
        episode = int(split[-1].split(".")[0])
        name = name + " - " "S%sE%02.d." % (s,episode) + split[-1]
        #name = name + " - " + split[2].split(".")[0] + "."+ split[-1].split(".")[-1]
        print "Renaming:   " + f + "    to:  " + name

        if int(sys.argv[2]) == 1:
            shutil.move(path + show + "/" + season + "/" + f, path + show + "/" + season + "/" + name)

        episode +=1
