import React from 'react'
import TableWithModal from '../components/TableWithModal'
import Wrapper from '../components/Wrapper'
const temperatureDisplay = (temperature) => (
  <span key={temperature}>{temperature} F</span>
)
const columns = [
  {
    title: 'Thermostats Name',
    dataIndex: 'thermostat_name',
    key: 'thermostat_name',
  },
  {
    title: 'Temperature',
    dataIndex: 'temperature',
    key: 'temperature',
    render: temperatureDisplay,
  },
]
const Thermostats = () => (
  <Wrapper title={'Thermostats'}>
    <TableWithModal
      columns={columns}
      eventKey={'thermostat'}
      key={'thermostat'}
      getKey={'thermostat'}
    />
  </Wrapper>
)
export default Thermostats
