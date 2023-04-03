from screenwriting.screenwriting import dur_type

def algorithmode():
  dur_type("You need to pee. The door to the bathroom is right in front of you, and the front door of your house is about 2 metres or 4 paces away. Don't let the position of the bathroom door fool you, however. This will not be as easy as you might think. As you have just started, you can only perform actions that correlate directly to body parts (or turn, or pee).")
  commands = ["turn:left","turn:right","hand:reach","hands:latch","hand:turn","hand:withdraw","leftfoot:stepforth","leftfoot:stepback","rightfoot:stepforth","rightfoot:stepback","feet:equalise","knees:bend","knees:straighten","waist:bend","waist:straighten"]
  dur_type("commands currently available:")
  print(commands)