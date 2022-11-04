import requests
import pandas as pd
from datetime import datetime
from zipfile import ZipFile
from io import BytesIO

#########################################
## Utils
#########################################

def create_data_frame(all_download_urls):

    """
    :param all_download_urls:
    :return:
    """

    # Create one dataframe with all URLs and time
    df = pd.DataFrame(data={"URL": all_download_urls})
    df['Date'] = df.URL.apply(lambda x: x.split('/')[-1].split('.')[0][:-6])
    df['Time_Stamp'] = df.URL.apply(lambda x: x.split('/')[-1].split('.')[0][-6:])
    df.Date = pd.to_datetime(df.Date,format="%Y%m%d")

    return df

def create_dict(x):

    """
    :param x:
    :return:
    """

    x2 = x.split(';')[:-1]
    d = {y.split(',')[0] : int(y.split(',')[1]) for y in x2}

    return d



def retrieve_and_save_files(download_url,output_directory,start_date,end_date):

    """
    :param download_url: string gdelt master file url
    :param output_directory: string file to output directory
    :param start_date: string YYYY-mm-dd start date for retrieval
    :param end_date: string YYYY-mm-dd end date for retrieval
    :return: saves on daily basis aggregated files as csv in output directory
    """

    # 1. Get all links
    all_download_data = requests.get(download_url).text.split('\n')[:-1]
    # Save only the gkg urls
    all_download_urls = [x.split(' ')[-1] for x in all_download_data if x.split(' ')[-1].split('.')[-3] == 'gkg']
    print('All download urls retrieved.')

    # 2. Crete data frame with all URLs and time stamp
    url_df = create_data_frame(all_download_urls)
    print('URL data frame created.')

    # 3. Filter by date range, aggregate and save daily files
    relevant_dates = pd.date_range(start_date,end_date)
    print('Start retrieving daily data')

    for date in relevant_dates:

        # Save date as string
        time_stamp = datetime.strftime(date, format="%Y%m%d")

        # Get all urls of one day
        daily_urls = url_df[url_df.Date == date].URL.tolist()
        n = len(daily_urls)

        # Load files of one day and concetanate them
        for i,file_url in enumerate(daily_urls):

            # Retrieve data from url
            i = i + 1
            print('Retrieve data for ' + time_stamp + ': URL ',i,'/', n)
            archive = requests.get(file_url)
            files = ZipFile(BytesIO(archive.content))

            # Get data
            try:
                data = pd.read_csv(files.open(files.filelist[0].filename),sep="\t",header=None,
                                   usecols = [1, 12, 14],encoding = 'utf-8')
            except UnicodeDecodeError:
                data = pd.read_csv(files.open(files.filelist[0].filename), sep="\t", header=None,
                                   usecols=[1,12, 14], encoding="ISO-8859-1")
            except:
                continue
            data.set_axis(gkg_headers, axis=1, inplace=True)

            # Drop nas
            data.dropna(inplace=True)

            # Format columns
            data.DATE = pd.to_datetime(data.DATE,format="%Y%m%d%H%M%S")
            data.PERSONS = data.PERSONS.apply(lambda x: create_dict(x))
            data.ORGANIZATIONS = data.ORGANIZATIONS.apply(lambda x: create_dict(x))

            if i == 1:
                daily_df = data
            else:
                daily_df = pd.concat([daily_df, data], axis=0)

        # Save daily aggregated file as csv
        print('Save daily dataframe.')
        daily_df.to_parquet(output_directory + '/GEG_daily_' + time_stamp + '.parquet',index=False)


###################################################################################
download_url = "http://data.gdeltproject.org/gdeltv2/masterfilelist.txt"
output_directory = "/Users/lucaslinden/Pythonkurs/GKG_Daten"
start_date = "2022-07-01"
end_date = "2022-07-01"
gkg_headers = ['DATE','PERSONS','ORGANIZATIONS']

retrieve_and_save_files(download_url,output_directory,start_date,end_date)







