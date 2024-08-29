<h1>Amharic Information Retrieval (IR) System</h1>

<h2>Overview</h2>
<p>
This project aims to develop an Amharic Information Retrieval (IR) system, focusing on methodologies and strategies to enhance search capabilities in the Amharic language. The system addresses challenges specific to Amharic text processing, such as morphological complexity and the need for efficient stemming techniques. By leveraging current research and findings from various studies, this project provides a comprehensive foundation for creating an effective Amharic IR system, enabling better access to information in this underrepresented language.
</p>

<h2>System Architecture</h2>
<p>The system architecture is composed of several interconnected modules designed for both document and query processing:</p>
<ol>
    <li>
        <strong>Tokenization Module:</strong> Splits the raw text of documents and queries into individual tokens (words), preparing them for further processing.
    </li>
    <li>
        <strong>Stemming Module:</strong> Applies a longest match stemming approach to reduce words to their root forms, removing prefixes and suffixes while handling infixes and plural forms.
    </li>
    <li>
        <strong>Stopword Removal Module:</strong> Removes common stopwords that carry little semantic weight (e.g., "እና", "ስለዚህ") from documents and queries.
    </li>
    <li>
        <strong>Indexing Module:</strong> Maps terms to their corresponding document identifiers, facilitating efficient retrieval. The indexed data is stored in <code>indexed_doc.json</code>.
    </li>
    <li>
        <strong>Term Weighting Module:</strong> Calculates the importance of each term relative to the entire document corpus using term frequency (TF) and inverse document frequency (IDF). The term weights are saved in <code>termWeights.json</code>.
    </li>
    <li>
        <strong>Term Matching (Searching) and Retrieval Module:</strong> Matches processed query tokens against indexed terms in the document corpus, retrieving the most relevant documents based on the computed term weights.
    </li>
</ol>

<h2>Implementation</h2>

<h3>Technologies Used</h3>

<h4>Programming Languages</h4>
<ul>
    <li><strong>Python:</strong> The primary language for development due to its simplicity, extensive libraries, and strong community support.</li>
</ul>

<h4>Libraries and Tools</h4>
<ul>
    <li><strong>BeautifulSoup:</strong> Used for web scraping to extract text data from the VOA Amharic website.</li>
    <li><strong>JSON:</strong> Utilized for storing indexed documents and term weights in <code>indexed_doc.json</code> and <code>termWeights.json</code>.</li>
    <li><strong>Flask:</strong> A web framework used to create the user interface for querying the document retrieval system, allowing user interaction via a web browser.</li>
</ul>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.x</li>
    <li>Flask</li>
    <li>BeautifulSoup4</li>
    <li>Requests</li>
</ul>

<h3>Installation</h3>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yisMeb/amharic_IR_system.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd amharic_IR_system</code></pre>
    </li>
    <li>Install the required Python packages:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
</ol>

<h3>Running the Application</h3>
<ol>
    <li>Start the Flask server:
        <pre><code>python main.py</code></pre>
    </li>
</ol>
