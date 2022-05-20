from os import *
from time import sleep
from random import randint
from PIL import Image
from os.path import isfile, join
size = 2000,2000
nb_items = 9

# Import assets
background_list = [f for f in listdir('1 - Background/') if isfile(join('1 - Background/', f))]
body_list = [f for f in listdir('2 - Body/') if isfile(join('2 - Body/', f))]
hair_list = [f for f in listdir('3 - Hair/') if isfile(join('3 - Hair/', f))]
eyes_list = [f for f in listdir('4 - Eyes/') if isfile(join('4 - Eyes/', f))]
mouth_list = [f for f in listdir('5 - Mouth/') if isfile(join('5 - Mouth/', f))]
clothe_list = [f for f in listdir('7 - clothes/') if isfile(join('7 - clothes/', f))]
accessory_list = [f for f in listdir('6 - Accessory/') if isfile(join('6 - Accessory/', f))]


# Display found assets in the console
print("-- Listed files --",
    "\n",
    background_list,
    "\n",
    body_list,
    "\n",
    hair_list,
    "\n",
    eyes_list,
    "\n",
    mouth_list,
    "\n",
    clothe_list,
    "\n",
    accessory_list,
    "\n",
    "----------------"
    )

generated_NFT = []
generated_ADN = []
def generate_ADN():
    for i in range(1,1501):
        adn = [randint(0,nb_items),randint(0,nb_items),randint(0,nb_items),randint(0,nb_items),randint(0,nb_items),randint(0,nb_items),randint(0,8)]
        items = [background_list[adn[0]],body_list[adn[1]],hair_list[adn[2]],eyes_list[adn[3]],mouth_list[adn[4]],clothe_list[adn[5]],accessory_list[adn[6]]]
        current_NFT = {"id": f"#{i}", "ADN": adn, "items":items}
        if adn in generated_ADN:
            continue
        generated_ADN.append(adn)
        generated_NFT.append(current_NFT)
    
def generate_NFT():
    # Create NFT images by merging corresponding items
    for nft in generated_NFT:
        print(f" ID : {nft['id']} | ADN : {nft['ADN']} | ITEMS : {nft['items']}")
        current_adn = nft['ADN']
        bg = Image.open(f'1 - Background/{background_list[current_adn[0]]}')
        skin = Image.open(f'2 - Body/{body_list[current_adn[1]]}')
        eyes = Image.open(f'4 - Eyes/{eyes_list[current_adn[3]]}')
        hair = Image.open(f'3 - Hair/{hair_list[current_adn[2]]}')
        mouth = Image.open(f'5 - Mouth/{mouth_list[current_adn[4]]}')
        clothing = Image.open(f'7 - clothes/{clothe_list[current_adn[5]]}')
        accessory = Image.open(f'6 - Accessory/{accessory_list[current_adn[6]]}')
        new_image = Image.new('RGB',(2000,2000), (250,250,250))
        new_image = Image.alpha_composite(bg,skin)
        new_image = Image.alpha_composite(new_image,eyes)
        new_image = Image.alpha_composite(new_image,mouth)
        new_image = Image.alpha_composite(new_image,clothing)
        new_image = Image.alpha_composite(new_image,accessory)
        new_image = Image.alpha_composite(new_image,hair)
        
        new_image.save(f"nft/{nft['id']}.png","PNG")
        new_image.close()
        print("-- GENERATED -- \n\n")


generate_ADN()
generate_NFT()