import React from 'react'
import Head from 'next/head'
const MainHead = ({ title }) => {
  return (
    <Head>
      <title>{title}</title>
      <meta charSet='utf-8' />
      <meta name='viewport' content='initial-scale=1.0, width=device-width' />
      <link
        rel='icon'
        type='image/png'
        sizes='16x16'
        href={'https://www.canoo.com/icons/icon-48x48.png'}
      />
      <link
        href='https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&display=swap'
        rel='stylesheet'
      />
    </Head>
  )
}
export default MainHead
