# index dictionary by list of key names

def start_loop():
	print("start")

def close_loop():
	print("close")

def pointer_right():
    print("right")

def pointer_left():
    print("left")

def cell_increment():
    print("increment")

   #how do i want to handle cell overflow?
   #should a cell that overflow go into the next cell?
   #i think that it should to better represent how binary works (so the computer can understand)
   #however it would be much easier to just reset at 255

def cell_decrement():
    print("decrement")
    #if i do handle overflow then should underflow be handled too?
    #eg cell_decrement.bf_tape_array[0]
    #where bf_tape_array[0]=0
    #this should underflow to 255
    #does the previous cell get subtracted by one?
    #if i do this make sure to check and see if its in the array

def print_byte():
    print("print")

def read_byte():
    print("read")


fndict = {
	"[":start_loop,
	"]":close_loop,
	">":pointer_right,
	"<":pointer_left,
	"+":cell_increment,
	"-":cell_decrement,
	".":print_byte,
	",":read_byte,
}

def fndict_caller(passed_instruction, tape_array):
	fndict[passed_instruction](tape_array)
	#how will the function handle changing the bf_tape_array location
	#have to return its ending location and value
	#need to recieve the tape_array at each subfunction


tape_array = [0,0,0,0,]



#how do i want to store the tape array?
#could just make a list of really long length
#could check everytime the cursor is supposed to move to the right
#also need to check when the cursor is going left to prevent it from going to bf_tape_array[-1]

#how do i keep track of the current tape array location
#is important to know for incrementing and decrementing


#how do i store the string that is recieved from the genetic swapping
#could store it as a string
# eg "+[><+-}"
#could store it as an array 
# eg string_array["+", "[", ">", "<", ...]
#could store it as an array of function locations
# eg func_array[print_byte, read_byte, ...]
# print func_array:
#[<function sample1 at 0x00000252A04B9400>, <function samplefunc at 0x000002529F9D7F28> ...]


#this needs some thought
#do i want to treat these as loops or quasi goto statements
#each [ could increment a counter which tracks which ] to go to
#similiarly for ]
#eg [ [!] ]
# ! is treated as a ] so the loop will reset back the first [
#also @[ ] asdf]
# @ is treated as a [ so it will skip to asdf if 
