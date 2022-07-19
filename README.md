# XML2TXT
Transfer annotations from **XML** to **TXT** for YOLO model.
## Usage
```bash
python main.py -directory_path
```
## Example
The raw XML file:
```xml
<annotation>
	<folder/>
	<filename>example1.jpeg</filename>
	<path>D:\example1.jpeg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>2396</width>
		<height>1600</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>house</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>750</xmin>
			<ymin>92</ymin>
			<xmax>1865</xmax>
			<ymax>753</ymax>
		</bndbox>
	</object>
	<object>
		<name>flower</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>307</xmin>
			<ymin>819</ymin>
			<xmax>1786</xmax>
			<ymax>1492</ymax>
		</bndbox>
	</object>
</annotation>
```
Output TXT file:
```text
0 0.545701 0.264062 0.465358 0.413125
1 0.436769 0.722187 0.617278 0.420625
```
The related file `classes.txt` will also be created.
