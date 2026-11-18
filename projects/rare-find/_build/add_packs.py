"""add_packs.py: adds the second set of prompt packs to packs.json, written by the author with Claude.

Each line is an answer; other names and spellings go in brackets: "Plane (airplane, aeroplane)".
Run once: python3 _build/add_packs.py. It skips any pack id already in packs.json.
"""
import json, os, re

here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, "packs.json")

def items(text):
    out = []
    for part in [x.strip() for x in text.split(";") if x.strip()]:
        m = re.match(r"^(.*?)\s*\((.*)\)$", part)
        out.append({"a": m.group(1).strip(), "aka": [a.strip() for a in m.group(2).split(",")]} if m else {"a": part, "aka": []})
    return out

NEW = [
 ("colour", "Name a colour", "General",
  "Red; Blue; Green; Yellow; Purple; Orange; Pink; Black; White; Brown",
  "Puce; Vermilion; Chartreuse; Cerulean; Gamboge",
  "Grey (gray); Teal; Turquoise; Magenta; Indigo; Violet; Maroon; Navy (navy blue); Beige; Gold; Silver; Crimson; Scarlet; Lavender; Lilac; Cyan; Olive; Lime; Tan; Cream; Ivory; Peach; Coral; Salmon; Burgundy; Aqua; Amber; Bronze; Khaki; Ochre; Sienna; Taupe; Fuchsia; Mauve; Mint; Emerald; Sapphire; Ruby; Charcoal; Plum; Rust; Sky blue; Mustard; Jade; Azure; Periwinkle; Copper; Cobalt; Ultramarine",
  "Rainbow; Glitter; Shiny", "Shades count, such as Teal."),
 ("zoo-animal", "Name a zoo animal", "Animals",
  "Lion; Elephant; Giraffe; Monkey; Tiger; Zebra; Penguin; Bear; Gorilla; Hippo (hippopotamus)",
  "Okapi; Tapir; Binturong; Aye-aye; Fossa",
  "Rhino (rhinoceros); Kangaroo; Koala; Panda (giant panda); Polar bear; Cheetah; Leopard; Jaguar; Flamingo; Ostrich; Crocodile; Alligator; Snake; Chimpanzee (chimp); Orangutan; Camel; Meerkat; Lemur; Sloth; Hyena; Wolf; Seal; Sea lion; Otter; Red panda; Komodo dragon; Tortoise; Peacock; Parrot; Baboon; Antelope; Bison; Wildebeest; Warthog; Llama; Alpaca; Armadillo; Anteater; Porcupine; Gazelle; Emu; Bat; Iguana; Python; Capybara; Gibbon; Hornbill; Pelican; Cassowary; Snow leopard",
  "Unicorn; Dragon; Dinosaur", ""),
 ("weather", "Name a type of weather", "General",
  "Rain (rainy); Snow (snowy); Sun (sunny, sunshine); Wind (windy); Storm (stormy); Fog (foggy); Hail; Thunder; Lightning; Cloud (cloudy, clouds)",
  "Graupel; Virga; Haboob; Diamond dust; Petrichor",
  "Sleet; Drizzle; Hurricane; Tornado; Blizzard; Heatwave (heat wave); Frost; Mist; Drought; Monsoon; Typhoon; Cyclone; Thunderstorm; Rainbow; Hailstorm; Sandstorm (dust storm); Gale; Breeze; Humidity; Smog; Ice storm; Freezing rain; Downpour; Shower (showers); Flood; Dew; Overcast; Squall; Whiteout; Waterspout; Black ice; Snowstorm; Cold snap; Heat; Haze; Clear sky (clear); Sun shower; Fog bank",
  "Earthquake; Volcano; Tsunami", ""),
 ("sandwich", "Name a sandwich", "Food",
  "BLT; Grilled cheese (cheese toastie); Ham and cheese; Peanut butter and jelly (PB&J, PBJ, peanut butter and jam); Club sandwich (club); Tuna (tuna mayo); Turkey; Egg salad (egg mayo); Reuben; Sub (submarine, hoagie)",
  "Francesinha; Bauru; Chivito; Mitraillette; Chip butty",
  "Cuban (cubano); Philly cheesesteak (cheesesteak); Banh mi; Panini; Croque monsieur; Po' boy (po boy); Monte Cristo; Sloppy joe; French dip; Meatball sub; Chicken salad; Egg and cress; Cheese and pickle; Fluffernutter; Muffuletta; Patty melt; Tuna melt; Bacon butty (bacon sandwich, bacon sarnie); Fish finger sandwich; Cucumber sandwich; Pastrami (pastrami on rye); Lobster roll; Torta; Katsu sando; Open sandwich (smorrebrod); Jam sandwich; Breakfast sandwich; Caprese; Toastie; Chicken parm; Roast beef; Prawn mayo; Coronation chicken; Egg and bacon; Ploughman's; Cheese sandwich; Ham sandwich; Chicken sandwich; Falafel wrap",
  "Pizza; Taco; Burrito", ""),
 ("sea-creature", "Name a sea creature", "Animals",
  "Shark; Whale; Dolphin; Octopus; Jellyfish; Starfish (sea star); Crab; Seahorse; Sea turtle (turtle); Lobster",
  "Nudibranch; Sea pig; Vampire squid; Ocean sunfish (mola mola, sunfish); Sea butterfly",
  "Squid; Seal; Sea lion; Walrus; Manatee; Dugong; Stingray (ray); Manta ray; Eel; Clownfish; Swordfish; Tuna; Shrimp (prawn); Clam; Oyster; Mussel; Sea urchin; Coral; Sea anemone (anemone); Barracuda; Pufferfish; Orca (killer whale); Narwhal; Beluga; Hammerhead; Krill; Plankton; Sea cucumber; Lionfish; Anglerfish; Cod; Salmon; Hermit crab; Sea otter; Barnacle; Cuttlefish; Nautilus; Marlin; Sardine; Mackerel; Halibut; Flounder; Sea snake; Blue whale; Humpback whale; Great white (great white shark); Moray eel; Scallop; Conch; Sea slug",
  "Frog; Hippo; Duck", ""),
 ("body-part", "Name a part of the body", "General",
  "Arm; Leg; Head; Hand; Foot (feet); Eye (eyes); Nose; Heart; Finger; Ear (ears)",
  "Philtrum; Lunula; Glabella; Hallux; Tragus",
  "Mouth; Knee; Elbow; Shoulder; Toe; Brain; Lung (lungs); Liver; Kidney; Stomach; Neck; Chest; Back; Hip; Ankle; Wrist; Thumb; Lip (lips); Tongue; Tooth (teeth); Hair; Skin; Chin; Cheek; Forehead; Eyebrow; Eyelash; Nail (fingernail, toenail); Knuckle; Heel; Spine; Rib; Skull; Bone; Muscle; Thigh; Calf; Shin; Belly button (navel); Jaw; Throat; Bladder; Pancreas; Appendix; Spleen; Gallbladder; Intestine (gut); Uvula; Earlobe; Armpit; Palm; Waist; Tendon; Collarbone; Kneecap; Eyelid; Nostril; Temple; Pinky (little finger)",
  "Wing; Fin; Antenna", ""),
 ("transport", "Name a way to travel", "General",
  "Car; Bus; Train; Plane (airplane, aeroplane); Bike (bicycle); Boat; Motorcycle (motorbike); Truck (lorry); Taxi (cab); Ship",
  "Funicular; Penny-farthing; Zeppelin (airship); Hovercraft; Velomobile",
  "Helicopter; Tram (streetcar); Subway (metro, underground, tube); Scooter; Skateboard; Van; Ferry; Submarine; Rocket; Hot air balloon (balloon); Canoe; Kayak; Sailboat (yacht); Tractor; Ambulance; Fire engine (fire truck); Limousine (limo); Jet ski; Snowmobile; Cable car; Rickshaw; Tuk-tuk; Monorail; Gondola; Unicycle; Tricycle; Glider; Blimp; Segway; Horse; Sled (sledge, sleigh); Raft; Golf cart; Spaceship (spacecraft, space shuttle); Roller skates (rollerblades); Quad bike (ATV); Electric scooter (e-scooter); Walking (on foot, walk); Coach; Minibus; Moped; Paddleboard; Rowing boat (rowboat); Hang glider; Parachute",
  "Road; Engine; Wheel", "On foot counts."),
 ("playground-game", "Name a playground game", "Games",
  "Tag (tig, it); Hide and seek (hide and go seek); Hopscotch; Skipping (jump rope); Red light green light; Simon says; Duck duck goose; Tug of war; Marbles; Four square",
  "Kick the can; Red rover; British bulldog (bulldog); Conkers; Elastics",
  "Freeze tag; Musical chairs; Sardines; Capture the flag; Dodgeball; Kickball; Leapfrog; Marco Polo; Hot potato; What's the time Mr Wolf; Statues; Follow the leader; Sack race; Egg and spoon race; Three-legged race; Rock paper scissors; Jacks; Hula hoop; Frisbee; Catch; Piggy in the middle (monkey in the middle); Tetherball; Handball; Wall ball; Stuck in the mud; Cops and robbers; Mother may I; Ring around the rosie (ring a ring o' roses); Blind man's buff; Musical statues; Grandma's footsteps; Chase; Clapping games; Slides (slide); Swings; Seesaw; Monkey bars; Football; Tag rugby; Hide the thimble; Sharks and minnows; Mannequin; Kiss chase",
  "Chess; Video games; Monopoly", ""),
 ("kitchen", "Name something in a kitchen", "General",
  "Fridge (refrigerator); Oven; Stove (cooker, hob); Sink; Microwave; Kettle; Toaster; Knife (knives); Spoon; Fork",
  "Mandoline; Spurtle; Mezzaluna; Chinois; Bain-marie",
  "Pan (frying pan); Pot (saucepan); Plate; Bowl; Cup; Mug; Glass; Dishwasher; Blender; Whisk; Spatula; Ladle; Colander; Cutting board (chopping board); Rolling pin; Grater; Peeler; Tongs; Can opener (tin opener); Corkscrew; Oven mitt (oven glove); Tea towel (dish towel); Apron; Cupboard (cabinet); Counter (worktop, countertop); Table; Chair; Bin (trash can); Sponge; Dish soap (washing-up liquid); Timer; Scales; Measuring cup; Sieve; Funnel; Baking tray; Muffin tin; Food processor; Mixer (stand mixer); Coffee maker; Teapot; Spice rack; Napkin; Tablecloth; Tap (faucet); Freezer; Grill; Wok; Casserole dish; Salt; Pepper; Bread bin; Chopsticks; Pressure cooker; Slow cooker; Air fryer; Garlic press; Pestle and mortar (mortar and pestle)",
  "Bed; Bath; Sofa", ""),
]

data = json.load(open(path, encoding="utf-8"))
have = {p["id"] for p in data["packs"]}
added = 0
for pid, prompt, cat, ranked, gems, good, wrong, note in NEW:
    if pid in have:
        continue
    p = {"id": pid, "prompt": prompt, "cat": cat, "ranked": items(ranked), "gems": items(gems), "good": items(good), "wrong": [w.strip() for w in wrong.split(";")]}
    if note:
        p["note"] = note
    assert len(p["ranked"]) == 10 and len(p["gems"]) == 5 and len(p["good"]) >= 20, pid
    data["packs"].append(p); added += 1
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("added", added, "packs; total", len(data["packs"]))
