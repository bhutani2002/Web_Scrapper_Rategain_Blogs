import React from 'react'
import Company_Logo from '../assets/RateGain_Logo.png'
const Navbar = () => {
  return (
    <div className='fixed top-0 left-0 bg-[#191919] p-4 text-white flex justify-between items-center w-full'>
        <div className='h-full w-full ml-12'>
            <img src = {Company_Logo} className='h-8' alt = "Rategain"/>
        </div>
    </div>
  )
}

export default Navbar