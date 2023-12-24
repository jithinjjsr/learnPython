from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("http://localhost:4200/workspace")

# title = driver.title
time.sleep(4) # take a pause 4 seconds
# driver.implicitly_wait(30)

# inputQuery = driver.find_element(by=By.ID, value="inputQuery")
# searchBtn = driver.find_element(by=By.ID, value="searchBtn")
# inputQuery.send_keys("Good will hunting")
st = "Predestination,Moving,We're the Millers,Are You There God? It's Me, Margaret.,Hunterrr,Freaky,Wedding Dress,3-Iron,Straw Dogs,Death Proof,I Care a Lot,Ready or Not,Sniper. The White Raven,Life Like,Good Night,Evaru,It's Kind of a Funny Story,Enemy,Level 16,Honor Society,Greta,Odd Thomas,Upgrade,Coherence,Devil in Ohio,The Glory,Behind Her Eyes,Maleficent,Athena,The Immaculate Room,The Unbearable Weight of Massive Talent,In the Tall Grass,Triangle of Sadness,Beau Is Afraid,The White Lotus,Barot House,Den of Thieves,Everything Everywhere All at Once,The Grand Budapest Hotel,Marcel the Shell with Shoes On,The Age of Shadows,The Departed,Jhimma,The Sting,The Boy in the Striped Pajamas,The Lobster,Saani Kaayidham,Teen Titans Go! To the Movies,Taanakkaran,The Gift,Pakal Nakshatrangal,The Clovehitch Killer,Kimi,One Flew Over the Cuckoo's Nest,The Last Boy Scout,Palm Springs,Before I Fall,The Tashkent Files,Sardar Udham,Tumbbad,Panic Room,Sometimes,Kasada Thapara,Waves,The Killing of Two Lovers,Mr. and Mrs. Iyer,Ravening,Lost in Translation,Uncut Gems,Molly's Game,Wind River,No Mercy,The Ballad of Buster Scruggs,Scarface,Top Gun,Spy Game,Enemy of the State,Crimson Tide,Calcutta News,C/O Kaadhal,Naalu Pennungal,Nomadland,I Am Not an Easy Man,The Man from Earth,Snowpiercer,When a Stranger Calls,The Witch: Part 1 - The Subversion,The Babadook,The Handmaiden,Fish Tank,The Flight Attendant,28 Weeks Later,Clue,I Saw the Devil"
arr = st.split(",")
# arr = ['Moving', "Are You There God? It's Me", 'Hunterrr', 'Wedding Dress', 'Straw Dogs', 'I Care a Lot', 'Sniper. The White Raven', 'Good Night', 'Evaru', "It's Kind of a Funny Story", 'Enemy', 'Level 16', 'Honor Society', 'Greta', 'Odd Thomas', 'Upgrade', 'Coherence', 'Devil in Ohio', 'The Glory', 'Behind Her Eyes', 'Maleficent', 'Athena', 'The Immaculate Room', 'The Unbearable Weight of Massive Talent', 'In the Tall Grass', 'Triangle of Sadness', 'Beau Is Afraid', 'The White Lotus', 'Barot House', 'Den of Thieves', 'Everything Everywhere All at Once', 'The Grand Budapest Hotel', 'Marcel the Shell with Shoes On', 'The Age of Shadows', 'The Departed', 'Jhimma', 'The Sting', 'The Boy in the Striped Pajamas', 'The Lobster', 'Saani Kaayidham', 'Teen Titans Go! To the Movies', 'Taanakkaran', 'The Gift', 'Pakal Nakshatrangal', 'The Clovehitch Killer', 'Kimi', "One Flew Over the Cuckoo's Nest", 'The Last Boy Scout', 'Palm Springs', 'Before I Fall', 'The Tashkent Files', 'Sardar Udham', 'Tumbbad', 'Panic Room', 'Sometimes', 'Kasada Thapara', 'Waves', 'The Killing of Two Lovers', 'Mr. and Mrs. Iyer', 'Ravening', 'Lost in Translation', 'Uncut Gems', "Molly's Game", 'Wind River', 'No Mercy', 'The Ballad of Buster Scruggs', 'Scarface', 'Top Gun', 'Spy Game', 'Enemy of the State', 'Crimson Tide', 'Calcutta News', 'C/O Kaadhal', 'Naalu Pennungal', 'Nomadland', 'I Am Not an Easy Man', 'The Man from Earth', 'Snowpiercer', 'When a Stranger Calls', 'The Witch: Part 1 - The Subversion', 'The Babadook', 'The Handmaiden', 'Fish Tank', 'The Flight Attendant', '28 Weeks Later', 'Clue', 'I Saw the Devil'] 
# arr = ["Are You There God? It's Me", 'Wedding Dress', 'I Care a Lot', 'Good Night', "It's Kind of a Funny Story", 'Level 16', 'Greta', 'Upgrade', 'Devil in Ohio', 'Behind Her Eyes', 'Athena', 'The Unbearable Weight of Massive Talent', 'Triangle of Sadness', 'The White Lotus', 'Den of Thieves', 'The Grand Budapest Hotel', 'The Age of Shadows', 'Jhimma', 'The Boy in the Striped Pajamas', 'Saani Kaayidham', 'Taanakkaran', 'Pakal Nakshatrangal', 'Kimi', 'The Last Boy Scout', 'Before I Fall', 'Sardar Udham', 'Panic Room', 'Kasada Thapara', 'The Killing of Two Lovers', 'Ravening', 'Uncut Gems', 'Wind River', 'The Ballad of Buster Scruggs', 'Top Gun', 'Enemy of the State', 'Calcutta News', 'Naalu Pennungal', 'I Am Not an Easy Man', 'Snowpiercer', 'The Witch: Part 1 - The Subversion', 'The Handmaiden', 'The Flight Attendant', 'Clue']
# arr = ["Are You There God? It's Me", 'Wedding Dress', 'I Care a Lot', 'Good Night', "It's Kind of a Funny Story", 'Level 16', 'Greta', 'Upgrade', 'Devil in Ohio', 'Behind Her Eyes', 'Athena', 'The Unbearable Weight of Massive Talent', 'Triangle of Sadness', 'The White Lotus', 'Den of Thieves', 'The Grand Budapest Hotel', 'The Age of Shadows', 'Jhimma', 'The Boy in the Striped Pajamas', 'Saani Kaayidham', 'Taanakkaran', 'Pakal Nakshatrangal', 'Kimi', 'The Last Boy Scout', 'Before I Fall', 'Sardar Udham', 'Panic Room', 'Kasada Thapara', 'The Killing of Two Lovers', 'Ravening', 'Uncut Gems', 'Wind River', 'The Ballad of Buster Scruggs', 'Top Gun', 'Enemy of the State', 'Calcutta News', 'Naalu Pennungal', 'I Am Not an Easy Man', 'Snowpiercer', 'The Witch: Part 1 - The Subversion', 'The Handmaiden', 'The Flight Attendant', 'Clue']
# arr = ['Wedding Dress', 'Good Night', 'Level 16', 'Upgrade', 'Behind Her Eyes', 'The Unbearable Weight of Massive Talent', 'The White Lotus', 'The Grand Budapest Hotel', 'Jhimma', 'Saani Kaayidham', 'Pakal Nakshatrangal', 'The Last Boy Scout', 'Sardar Udham', 'Kasada Thapara', 'Ravening', 'Wind River', 'Top Gun', 'Calcutta News', 'I Am Not an Easy Man', 'The Witch: Part 1 - The Subversion', 'The Flight Attendant']
# arr =['Good Night', 'Upgrade', 'The Unbearable Weight of Massive Talent', 'The Grand Budapest Hotel', 'Saani Kaayidham', 'The Last Boy Scout', 'Kasada Thapara', 'Wind River', 'Calcutta News', 'The Witch: Part 1 - The Subversion']
print(arr)
rem = arr.copy()
for item in arr:
    # time.sleep(4)
    driver.implicitly_wait(4)
    inputQuery = driver.find_element(by=By.ID, value="inputQuery")
    searchBtn = driver.find_element(by=By.ID, value="searchBtn")
    inputQuery.send_keys(item)
    # time.sleep(4) # take a pause 4 seconds
    driver.implicitly_wait(4)
    searchBtn.click()
    time.sleep(1) # take a pause 4 seconds
    driver.implicitly_wait(4)
    try:
        loveBtn = driver.find_element(by=By.ID, value="loveBtn")
        loveBtn.click()
    except:
        print(item,' not found------')
    # time.sleep(4) # take a pause 4 seconds
    driver.implicitly_wait(4)
    rem.remove(item)
    inputQuery.clear()
    print(rem)
# driver.implicitly_wait(12.5)
print('-------------------------------')
print(rem)


['Moving', "Are You There God? It's Me", 'Hunterrr', 'Wedding Dress', 'Straw Dogs', 'I Care a Lot', 'Sniper. The White Raven', 'Good Night', 'Evaru', "It's Kind of a Funny Story", 'Enemy', 'Level 16', 'Honor Society', 'Greta', 'Odd Thomas', 'Upgrade', 'Coherence', 'Devil in Ohio', 'The Glory', 'Behind Her Eyes', 'Maleficent', 'Athena', 'The Immaculate Room', 'The Unbearable Weight of Massive Talent', 'In the Tall Grass', 'Triangle of Sadness', 'Beau Is Afraid', 'The White Lotus', 'Barot House', 'Den of Thieves', 'Everything Everywhere All at Once', 'The Grand Budapest Hotel', 'Marcel the Shell with Shoes On', 'The Age of Shadows', 'The Departed', 'Jhimma', 'The Sting', 'The Boy in the Striped Pajamas', 'The Lobster', 'Saani Kaayidham', 'Teen Titans Go! To the Movies', 'Taanakkaran', 'The Gift', 'Pakal Nakshatrangal', 'The Clovehitch Killer', 'Kimi', "One Flew Over the Cuckoo's Nest", 'The Last Boy Scout', 'Palm Springs', 'Before I Fall', 'The Tashkent Files', 'Sardar Udham', 'Tumbbad', 'Panic Room', 'Sometimes', 'Kasada Thapara', 'Waves', 'The Killing of Two Lovers', 'Mr. and Mrs. Iyer', 'Ravening', 'Lost in Translation', 'Uncut Gems', "Molly's Game", 'Wind River', 'No Mercy', 'The Ballad of Buster Scruggs', 'Scarface', 'Top Gun', 'Spy Game', 'Enemy of the State', 'Crimson Tide', 'Calcutta News', 'C/O Kaadhal', 'Naalu Pennungal', 'Nomadland', 'I Am Not an Easy Man', 'The Man from Earth', 'Snowpiercer', 'When a Stranger Calls', 'The Witch: Part 1 - The Subversion', 'The Babadook', 'The Handmaiden', 'Fish Tank', 'The Flight Attendant', '28 Weeks Later', 'Clue', 'I Saw the Devil'] 



# message = driver.find_element(by=By.ID, value="message")
# text = message.text

driver.quit()