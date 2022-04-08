//JDBC program to insert values into tables using PreparedStatement object
import java.util.*;
import java.sql.*;
class PreparedStatementDemo
{
	public static void main(String kjh[]) throws Exception
	{
		Scanner sc=new Scanner(System.in);
		Class.forName("oracle.jdbc.driver.OracleDriver");
		Connection con=DriverManager.getConnection("jdbc:oracle:thin:@ntsocietyserver:1521:oralbrce","IPC83","IPC83");
		/*System.out.println("How many records you want to insert?");
		int n=sc.nextInt();
		for(int i=0;i<n;i++)
		{
			PreparedStatement ps=con.prepareStatement("insert into Employees values(?,?,?)");
			System.out.println("Enter id of Employee : ");
			int id=sc.nextInt();
			ps.setInt(1,id);
			System.out.println("Enter name of Employee: ");
			String name=sc.next();
			ps.setString(2,name);
			System.out.println("Enter mobile number of Employee: ");
			String mob=sc.next();
			ps.setString(3,mob);
			System.out.println("No.of records upated is: "+ps.executeUpdate());
		}*/
		System.out.println("Enter id of Employee to delete: ");
		int n=sc.nextInt();
		PreparedStatement ps=con.prepareStatement("delete from Employees where eid="+n);
		ps.execute();
	}
}