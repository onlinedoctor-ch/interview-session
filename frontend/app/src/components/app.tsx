import React from "react";
import { HealthChecker } from "./HealthChecker";
import { Box, ChakraProvider, Flex, Heading, Text } from "@chakra-ui/react";

export const App: React.FC = () => {
  return (
    <ChakraProvider>
      <Layout>
        <Heading size="md">OnlineDoctor Basic Interview App</Heading>
        <HealthChecker />
      </Layout>
    </ChakraProvider>
  );
};

export const Layout: React.FC<React.PropsWithChildren<{}>> = ({ children }) => {
  return (
    <Flex flexDir="column">
      <Flex flexDir="row" bgColor="lightblue" p={4}>
        <Heading>OnlineDoctor</Heading>
      </Flex>
      <Box p={4}>{children}</Box>
    </Flex>
  );
};
