import requests
import pandas as pd
from datetime import datetime
from zipfile import ZipFile
from io import BytesIO


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


def retrieve_day(params):

    #Get params
    date = params['date']
    url_df = params['url_df']
    output_directory = params['output_directory']
    gkg_headers = params['gkg_headers']

    # Save date as string
    time_stamp = datetime.strftime(date, format="%Y%m%d")

    # Get all urls of one day
    daily_urls = url_df[url_df.Date == date].URL.tolist()
    n = len(daily_urls)

    # Load files of one day and concetanate them
    for i, file_url in enumerate(daily_urls):

        # Retrieve data from url
        i = i + 1
        print('Retrieve data for ' + time_stamp + ', URL: ',file_url,'(', i, '/', n,')')
        archive = requests.get(file_url)
        files = ZipFile(BytesIO(archive.content))

        # Get data
        try:
            data = pd.read_csv(files.open(files.filelist[0].filename), sep="\t", header=None,
                               usecols=[1, 12, 14], encoding='utf-8')
        except UnicodeDecodeError:
            data = pd.read_csv(files.open(files.filelist[0].filename), sep="\t", header=None,
                               usecols=[1, 12, 14], encoding="ISO-8859-1")
        except:
            continue
        data.set_axis(gkg_headers, axis=1, inplace=True)

        # Drop nas
        data.dropna(inplace=True)

        # Format columns
        data.DATE = pd.to_datetime(data.DATE, format="%Y%m%d%H%M%S")
        data.PERSONS = data.PERSONS.apply(lambda x: create_dict(x))
        data.ORGANIZATIONS = data.ORGANIZATIONS.apply(lambda x: create_dict(x))

        if i == 1:
            daily_df = data
        else:
            daily_df = pd.concat([daily_df, data], axis=0)

    # Save daily aggregated file as csv
    print('Save daily dataframe.')
    daily_df.to_parquet(output_directory + '/GEG_daily_' + time_stamp + '.parquet', index=False)
