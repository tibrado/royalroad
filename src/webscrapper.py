# Web Scrapper for python 
# Imports 
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from string import punctuation
import glob

class WebRunner:
    def __init__(self, driver_path = None, website = None, find = None, pause = 2):
        self.chrome_driver = self.driver(driver_path)
        self.setup = self.website(website)
        self.find = find
        self.data = set()
        self.pause = pause

    def driver(self, path):
        # Set up driver options. "How driver should run"
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')

        try:    
            return webdriver.Chrome(path, options = options)
        except:
            print('Failed to initialize driver')
            return None

    def website(self, site):
        if site: 
            try: 
                self.chrome_driver.get(site)
                self.setup = True
                return self.setup
            except:
                return False
        return False
    
    def element(self, find):
        self.find = find

    # Scroll throught page 
    def scroll(self, wait):
        current = self.chrome_driver.execute_script("return document.body.scrollHeight;")  # Current scroll height 

        # Scroll through screen 
        while True:
            self.chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll down 
            time.sleep(wait) # wait for page to load

            nh = self.chrome_driver.execute_script("return document.body.scrollHeight;")  # Current scroll height

            # Check if height is still the same if True the exit 
            if nh == current:
                break 
            current = nh 

            print(f'Scrolling: {nh}')


    def run(self, find = None, inf_scroll = False):
        # Set up element to find 
        if find: self.element(find)

        # Scroll window 
        if inf_scroll: self.scroll(self.pause)

        # Open file to write 
        file = open('scrape_data.txt', 'a')

        # Write to document 
        for page in range(2, 150):
            data = []

            for i in range(1, 21):
                try: 
                    book = self.get_info(i)
                    row = ';'.join(book)
                    data.append(row)
                except:
                    print(f'Book {i} Not Found')
            
            str_data = '\n'.join(data)

            # Write data to file 
            try: 
                file.write(str_data)
            except:
                print("Could not write into file")
        
            # Go to next page 
            try: 
                link = self.chrome_driver.find_element_by_link_text(f'{page}')
                link.click()
                print(f"Page: {page}-----------------------------------------------")
                time.sleep(1) # wait for page to load
            except: 
                break


        

        # Close File and web drive and file when done 
        file.close()
        self.chrome_driver.close()


    def get_info(self, index):

        '''
        Param: Int, intirate through the book info 
        Return: List Book details 
        '''

        title = self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/h2').text
        print(f'Title {index}: {title}')


        # Click tags button 
        self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/div[1]/span[2]/label').click()

        tags = ''
        for i in range(1, 20):
            try: 
                tags += self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/div[1]/span[2]/a[{i}]').text + '|'
            except:
                break

        followers = self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/div[2]/div[1]').text

        rating = self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/div[2]/div[2]').get_attribute("outerHTML").split('Rating: ')[1]
        rating = rating.split(' out')[0]

        pages = self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/div[2]/div[3]').text
        views = self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/div[2]/div[4]').text
        chapters = self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/div[2]/div[5]').text
        date_last_active = self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{index}]/div/div[2]/div[6]').text

        return [title, tags, followers, rating, pages, views, chapters, date_last_active]


    def get_book_info(self):
        entries = self.chrome_driver.find_element_by_class_name('dataTable-info').text.split('of ')[1]
        entries = int(entries.split('entries')[0])
        
        #print(f'- Entries: {entries}')
        # get only 5 chapters 
        if entries > 5: entries = 5
        

        #print('-- Warning')
        warnings = self.chrome_driver.find_element_by_class_name('list-inline').text
        
        #print('--- Summary')
        summary = self.chrome_driver.find_element_by_class_name('description').text

        """
        # ratings / Statictics 
        overall = 
        style = 
        story =
        grammer = 
        character = 
        """

        # Get chapters 
        chapters = [None, None, None, None, None]

        # Go to chapter 1
        # print('--- Chapter 1')
        self.chrome_driver.find_element_by_xpath(f'//*[@id="chapters"]/tbody/tr[1]').click()
        time.sleep(1) # wait for page to load

        try: 
            chapters[0] = self.chrome_driver.find_element_by_class_name('chapter-content').text
        except: 
            print('---- Failed')

        for i in range(1, entries):
            # Go to Chapter
            #print(f'---- Chapter {i + 1}')
            self.chrome_driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[3]/div[2]/div[1]/div[2]').click()
            time.sleep(2) # wait for page to load

            try: 
                chapters[i] = self.chrome_driver.find_element_by_class_name('chapter-content').text
            except: 
                print('---- Failed: ')

        
        return (warnings, summary, chapters)

    def click_book(self, page_at = 1, start_at = 0):
        page = page_at

        while page < 150:
            website = f'https://www.royalroad.com/fictions/active-popular?page={page}'

            # Go to next page 
            try: 
                self.chrome_driver.get(website)
                print(f"Page: {page}-----------------------------------------------")
                time.sleep(1) # wait for page to load
            except: 
                break

            # Get contenet 
            if start_at != 0:
                i = start_at
                start_at = 0

            while i < 20:
                title = self.chrome_driver.find_elements_by_class_name('fiction-title')[i].text
                #self.chrome_driver.find_elements_by_class_name('fiction-title')[i].click()

                self.chrome_driver.find_element_by_xpath(f'//*[@id="result"]/div[{i + 1}]/div/h2/a').click()
                print(f'Reading: {title}')

                # Load page 
                time.sleep(1)

                # Get book info 
                warnings, summary, chapters = self.get_book_info()

                # Open file to write 
                file = open(f'book{page}_{i}.txt', 'a')

                try:
                    file.write(title + f' {page}_{i} \n\n<;>\n\n\n')
                    file.write(warnings + '\n\n<;>\n\n\n')
                    file.write(summary + '\n\n<;>\n\n\n')
                    file.write('\n\n<;>\n\n\n'.join(chapters))
                except:
                    print('Fail To Write')
                
                file.close()

                # Go back to main page 
                self.chrome_driver.get(website)
                time.sleep(1) # wait for page to load

                i += 1
            # Go to next page         
            page += 1
            i = 0

                


'''
crawl = WebRunner('/media/noel/USB Drive/DS/Drivers/chromedriver', website = 'https://www.royalroad.com/fictions/active-popular?page=3')  
crawl.click_book(11, 13)
crawl.chrome_driver.quit()
'''

def get_page_book():
    last_book = glob.glob('*.txt')[-1]

    _page = last_book.strip('book').split('_')[0]
    _book = last_book.split('_')[1].strip('.txt')

    return (int(_page), int(_book))

trials = 0
book_failed_at = [None, None]
page_ = 54
book_ = 17

while True:
    try: 
        crawl = WebRunner('/media/noel/USB Drive/DS/Drivers/chromedriver', website = 'https://www.royalroad.com/fictions/active-popular?page=51')  
        crawl.click_book(page_, book_)
        crawl.chrome_driver.quit()
        break
    except:
        crawl.chrome_driver.quit() # stop driver 

        # Get last book read
        page_, book_ = get_page_book()
        book_ += 1

        if book_ == 20:
            book_ = 0
            page_ += 1

        trials += 1

        print(f'Failed to get page: {page_} book: {book_} attemp: #{trials}')

    # Move to next book 
    if (trials == 2):
        book_ += 1
        book_failed_at[0] = page_ 
        book_failed_at[1] = book_

        trials = 0


