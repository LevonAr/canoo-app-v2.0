import React, { useEffect } from 'react'
import Router from 'next/router'
import '../styles/globals.css'
import 'antd/dist/antd.css'
const MyApp = ({ Component, pageProps }) => {
  useEffect(() => Router.push('/lights'), [])
  return <Component {...pageProps} />
}
export default MyApp
