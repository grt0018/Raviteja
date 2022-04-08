import java.util.*;
import java.sql.*;
class Retrive
{
	public static void main(String kj[]) throws Exception
	{
		Scanner sc=new Scanner(System.in);
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con=DriverManager.getConnection("jdbc:oracle:thin:@ntsocietyserver:1521:oralbrce","IPC83","IPC83");
		Statement s=con.createStatement();
		s.execute("drop table Employees");
		System.out.println("Employees table dropped successfully");
		s.execute("create table Employees(eid int primary key,name varchar(20),mob varchar(10))");
		System.out.println("Employees table created successfully");
		s.execute("insert into Employees values(1,'Raki',9756234807)");
		s.execute("insert into Employees values(2,'Raviteja',9121025028)");
		s.execute("insert into Employees values(3,'Manikanta',9678542468)");
		System.out.println("Data inserted into table successfully");
		System.out.println("Enter Employee id");
		int empid=sc.nextInt();
		ResultSet r=s.executeQuery("select *from Employees where eid="+empid);
		boolean result=false;
		while(r.next())
		{
			//checks the rows line by line until all the records are complete
			System.out.println("You are a valid user");
			System.out.println("Hello "+r.getString(2));
			result=true;
		}
		if(result==false)
		{
			System.out.println("Invalid user");
		}
	}
}