import pandas as pd
import xml.etree.ElementTree as ET

extension = '0004PR'

def parse_xml_to_dataframe(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # List to hold the data
    data = []

    # Extract Positions element
    positions = root.find('Positions')
    
    # Extract the EventTime
    event_time = positions.attrib.get('EventTime', 'N/A')
    
    # Extract MetaData (assuming it's the same for all data)
    metadata = positions.find('MetaData')
    match_id = metadata.attrib.get('MatchId', 'N/A')
    pitch_size = metadata.find('PitchSize')
    pitch_x = pitch_size.attrib.get('X', 'N/A')
    pitch_y = pitch_size.attrib.get('Y', 'N/A')

    # Iterate through each FrameSet in the XML
    for frameset in positions.findall('FrameSet'):
        game_section = frameset.get('GameSection', 'N/A')
        team_id = frameset.get('TeamId', 'N/A')
        person_id = frameset.get('PersonId', 'N/A')
        
        # Iterate through each Frame in the FrameSet
        for frame in frameset.findall('Frame'):
            frame_number = frame.get('N', 'N/A')
            timestamp = frame.get('T', 'N/A')
            x_position = frame.get('X', 'N/A')
            y_position = frame.get('Y', 'N/A')
            distance = frame.get('D', 'N/A')
            speed = frame.get('S', 'N/A')
            acceleration = frame.get('A', 'N/A')
            minute = frame.get('M', 'N/A')
            
            # Append the data to the list
            data.append({
                'EventTime': event_time,
                'MatchId': match_id,
                'GameSection': game_section,
                'TeamId': team_id,
                'PersonId': person_id,
                'FrameNumber': frame_number,
                'TimeStamp': timestamp,
                'x-Position': x_position,
                'y-Position': y_position,
                'Distance': distance,
                'Speed': speed,
                'Acceleration': acceleration,
                'Minute': minute,
                'PitchX': pitch_x,
                'PitchY': pitch_y
            })

    # Create a DataFrame from the list of data
    df = pd.DataFrame(data)
    return df

# Usage example
xml_file = '/Users/dylantellado/Documents/Nashville Internship/test-tracking-data/test_tracking_data_MLS-MAT-0004PR.xml'
df = parse_xml_to_dataframe(xml_file)


df.to_csv(f'tracking_data_{extension}.csv', index=False)

