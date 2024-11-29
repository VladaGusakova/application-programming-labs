import pandas as pd
import cv2
import matplotlib.pyplot as plt
import argparse
import os

def create_parse () -> argparse.Namespace:
    '''
    Reads args from the terminal
    :return args: args for terminal
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("annotation_path", type = str, help = "Path to annotation")
    parser.add_argument("width", type = int, help = "Max width")
    parser.add_argument("height", type = int, help="Max height")
    args = parser.parse_args()
    return args


def create_df(annotation_path : str) -> pd.DataFrame:
    '''
    Creates DataFrame
    :param annotation_path: Path to annotation
    :return: DataFrame
    '''
    if os.path.isfile(annotation_path):
        df = pd.read_csv(annotation_path)
        return df
    else:
        raise FileNotFoundError(f"File {annotation_path} not found.")


def add_image_shape(df : pd.DataFrame) -> pd.DataFrame:
    '''
    Create column with height, width and channels of image
    :param df: Our DataFrame
    :return: Updated DataFrame
    '''
    height, width, channels = [],[],[]
    for path in df["relative path"]:
        img = cv2.imread(path)
        if os.path.isfile(path):
            height.append(img.shape[0])
            width.append(img.shape[1])
            channels.append(img.shape[2])
        else:
            raise FileNotFoundError(f"File {path} not found.")
    df["height"] = height
    df["width"] = width
    df["channels"] = channels
    return df


def statistic (df : pd.DataFrame) -> pd.DataFrame:
    '''
    Calculating statistics for dimensions
    :param df: Our DataFrame
    :return: None
    '''
    stats= df[["height", "width", "channels"]].describe()
    return stats


def filter_by_width_and_height (df: pd.DataFrame, max_w : int, max_h : int) -> pd.DataFrame:
    '''
    Filters DataFrame by width and height
    :param df: Our DataFrame
    :param max_w: Max width of image
    :param max_h: Max height of image
    :return: new DataFrame
    '''
    filtered_df = df[(df['width'] <= max_w) & (df['height'] <= max_h)]
    return filtered_df


def add_area(df : pd.DataFrame) -> pd.DataFrame:
    '''
    Add area of image
    :param df: Our DataFrame
    :return: DF with area
    '''
    if 'width' in df.columns:
        df['area'] = df['width'] * df['height']
        return df
    else:
        raise KeyError(f"Column 'width' and 'height' does not exist in DataFrame")


def filter_by_area(df : pd.DataFrame) -> pd.DataFrame:
    '''
    Calculates the area of image
    :param df: Our DataFrame
    :return: Sorted DataFrame
    '''
    if 'area' in df.columns:
        df_sorted = df.sort_values(by = 'area')
        return df_sorted
    else:
        raise KeyError(f"Column 'area' does not exist in DataFrame")


def create_histogram (df : pd.DataFrame) -> None :
    '''
    Creates a histogram relative to the area of the images
    :param df: Our DataFrame
    :return: None
    '''
    plt.hist(df['area'], bins = df.shape[0], edgecolor = 'black')
    plt.title('image area distribution')
    plt.xlabel('area (px)')
    plt.ylabel('frequency')
    plt.show()


def main () -> None:
    '''
    Use all functions
    :return: None
    '''
    try:
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        args = create_parse()
        df = create_df(args.annotation_path)
        print(df.head())
        add_image_shape(df)
        print(df, "\n")
        print(statistic(df))
        print(filter_by_width_and_height(df, args.width, args.height))
        print(filter_by_area(add_area(df)))
        create_histogram(df)
    except Exception as exc:
        print(exc)



if __name__ == '__main__':
    main()

