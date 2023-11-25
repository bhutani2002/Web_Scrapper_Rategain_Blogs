import './App.css';
import Banner from './components/Banner';
import Navbar from './components/Navbar';
import Scrape_Body from './components/Scrape_Body';

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Banner/>
      <Scrape_Body/>
    </div>
  );
}

export default App;
