import Retrieval_Utils as ru
import pandas as pd
import multiprocessing as mp
import requests

# Define daily retrieval and filterting as process
class Worker(mp.Process):

    def __init__(self,job_queue):

        super().__init__()

        # Initialize one attribute for worker (job_queue equals parameters of retrieve_GKG_day function)
        self._job_queue = job_queue

    # Define method
    def run(self):

        success_rates = []
        while True:

            # Get paramters from queue
            params = self._job_queue.get()

            # Stop if no dates left
            if len(params) == 0:
                break

            # Else: retrieve GKG daily file
            ru.retrieve_day(params)



if __name__ == "__main__":

    ########################
    ### input parameters ###
    ########################

    download_url = "http://data.gdeltproject.org/gdeltv2/masterfilelist.txt"
    output_directory = "/Users/lucaslinden/Pythonkurs/GKG_Daten"
    start_date = "2022-08-01"
    end_date = "2022-08-31"
    gkg_headers = ['DATE', 'PERSONS', 'ORGANIZATIONS']
    active_cores = mp.cpu_count()-3

    # 1. Get all links
    all_download_data = requests.get(download_url).text.split('\n')[:-1]
    # Save only the gkg urls
    all_download_urls = [x.split(' ')[-1] for x in all_download_data if x.split(' ')[-1].split('.')[-3] == 'gkg']
    print('All download urls retrieved.')

    # 2. Crete data frame with all URLs and time stamp
    url_df = ru.create_data_frame(all_download_urls)
    print('URL data frame created.')

    ########################################################################################################################
    # 3. Retrieve data

    # Get relevant dates
    relevant_dates = pd.date_range(start_date, end_date)

    # Initialize empty job list and empty queue
    jobs = []
    job_queue = mp.Queue()

    # Start as many workers as active cores
    for i in range(active_cores):
        p = Worker(job_queue)
        jobs.append(p)
        p.start()

    # Put job into queue
    for date in relevant_dates:
        job_queue.put({'date': date,
                       'url_df': url_df,
                       'output_directory':output_directory,
                       'gkg_headers': gkg_headers
                       })

    # Start as many workers as active cores
    for i in range(active_cores):
        p = Worker(job_queue)
        jobs.append(p)
        p.start()

    # Stop if all dates in queue (therefore append lists with none)
    for j in jobs:
        job_queue.put([])

    for job in jobs:
        p.join()
